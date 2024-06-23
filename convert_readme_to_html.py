import markdown
import re
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.extra import ExtraExtension
from bs4 import BeautifulSoup

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

# Function to convert plain URLs to markdown links outside of code blocks and HTML tags
def convert_urls_to_links(text):
    def replace(match):
        url = match.group(0)
        return f'<a href="{url}">{url}</a>'
    
    # Pattern to identify URLs outside of code blocks and HTML tags
    url_pattern = re.compile(r'(?<![`">])(https?://[^\s`"<]+)(?![<`])')
    return url_pattern.sub(replace, text)

# Function to process the markdown content and convert it to HTML
def process_markdown_to_html(input_file, intermediate_file, output_file):
    # Adjust code blocks
    adjust_code_blocks(input_file, intermediate_file)
    
    # Read the adjusted markdown file
    with open(intermediate_file, 'r') as file:
        readme_text = file.read()
    
    # Convert markdown to HTML with preserved code blocks, <br> tags for line breaks, and URL handling
    html_content = markdown.markdown(readme_text, extensions=[FencedCodeExtension(), Nl2BrExtension(), ExtraExtension()])
    
    # Parse the HTML content with BeautifulSoup to ensure no alteration to existing HTML tags and attributes
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Ensure all <pre><code> tags are correctly formatted
    for pre in soup.find_all('pre'):
        if pre.code:
            code_block = pre.code
            code_block.string = '\n' + code_block.string.strip() + '\n'
    
    # Convert URLs to links outside of code blocks and HTML tags
    for text_node in soup.find_all(string=True):
        if text_node.parent.name not in ['code', 'pre']:
            new_text = convert_urls_to_links(text_node)
            text_node.replace_with(BeautifulSoup(new_text, 'html.parser'))
    
    # Write the final HTML content to a new file
    with open(output_file, 'w') as file:
        file.write(soup.prettify())

    print(f"Conversion complete. The HTML content has been saved to {output_file}")

# Example usage
input_file = 'Readme.md'
intermediate_file = 'Readme_converted.md'
output_file = 'Readme.html'
process_markdown_to_html(input_file, intermediate_file, output_file)