import markdown
import html
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions.extra import ExtraExtension
from bs4 import BeautifulSoup
import re

# Function to adjust code blocks in the markdown file
def adjust_code_blocks(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.readlines()
    
    adjusted_content = []
    inside_code_block = False
    
    for line in content:
        if line.lstrip().startswith("```"):
            inside_code_block = not inside_code_block
            adjusted_content.append(line.lstrip())
        elif inside_code_block:
            adjusted_content.append(line)
        else:
            adjusted_content.append(line)
    
    with open(output_file, 'w') as file:
        file.writelines(adjusted_content)

# Function to convert GitHub image URLs to raw GitHub content URLs
def convert_github_image_urls(text):
    def replace(match):
        alt_text = match.group(1)
        url = match.group(2)
        if "github.com" in url and "/blob/" in url:
            raw_url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
            return f'![{alt_text}]({raw_url})'
        return match.group(0)
    
    image_pattern = re.compile(r'!\[([^\]]*)\]\((https?://[^\)]+)\)')
    return image_pattern.sub(replace, text)

# Function to convert Markdown image links to HTML <img> tags
def convert_images_to_html(text):
    image_pattern = re.compile(r'!\[([^\]]*)\]\((https?://[^\)]+)\)')
    return image_pattern.sub(r'<img class="d-block w-100" alt="\1" src="\2" />', text)

# Function to process the markdown content and convert it to HTML
def process_markdown_to_html(input_file, intermediate_file, output_file):
    # Adjust code blocks
    adjust_code_blocks(input_file, intermediate_file)
    
    # Read the adjusted markdown file
    with open(intermediate_file, 'r') as file:
        readme_text = file.read()
    
    # Convert GitHub image URLs to raw GitHub content URLs
    readme_text = convert_github_image_urls(readme_text)
    
    # Convert Markdown image links to HTML <img> tags
    readme_text = convert_images_to_html(readme_text)
    
    # Convert markdown to HTML with preserved code blocks, <br> tags for line breaks, and URL handling
    html_content = markdown.markdown(readme_text, extensions=[FencedCodeExtension(), Nl2BrExtension(), ExtraExtension()])
    
    # Parse the HTML content with BeautifulSoup to ensure no alteration to existing HTML tags and attributes
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Escape HTML entities in code blocks to ensure they are displayed correctly
    for code_block in soup.find_all('code'):
        if code_block.string:
            escaped_code = html.escape(code_block.string)
            code_block.string.replace_with(escaped_code)
    
    # Write the final HTML content to a new file
    with open(output_file, 'w') as file:
        file.write(soup.prettify(formatter=None))

    print(f"Conversion complete. The HTML content has been saved to {output_file}")

# Example usage
input_file = 'Readme.md'
intermediate_file = 'Readme_converted.md'
output_file = 'Readme.html'
process_markdown_to_html(input_file, intermediate_file, output_file)