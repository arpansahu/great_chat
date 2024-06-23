import markdown
import re
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions.extra import ExtraExtension
from bs4 import BeautifulSoup

# Adjust code blocks to remove leading spaces from code block markers
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

# Convert plain URLs to markdown links outside of code blocks and HTML tags
def convert_urls_to_links(html_content):
    def replace(match):
        url = match.group(0)
        return f'<{url}>'
    
    # Pattern to identify URLs outside of code blocks and HTML tags, but not within attributes
    url_pattern = re.compile(r'(?<![`">])((?<!src=["\'])https?://[^\s`"<]+)(?![<`])')
    return url_pattern.sub(replace, html_content)

# Main script for conversion
def main():
    input_file = 'Readme.md'
    intermediate_file = 'Readme_converted.md'
    output_file = 'Readme.html'

    # Adjust code blocks in the input file
    adjust_code_blocks(input_file, intermediate_file)

    # Read the adjusted contents of the intermediate file
    with open(intermediate_file, 'r') as file:
        readme_text = file.read()

    # Convert markdown to HTML with preserved code blocks, <br> tags for line breaks, and URL handling
    html_content = markdown.markdown(readme_text, extensions=[FencedCodeExtension(), Nl2BrExtension(), ExtraExtension()])

    # Parse the HTML content with BeautifulSoup to ensure no alteration to existing HTML tags and attributes
    soup = BeautifulSoup(html_content, 'html.parser')

    # Fix code blocks not being rendered correctly
    for pre_block in soup.find_all('pre'):
        if pre_block.code:
            code_block = pre_block.code
            # Ensure the first line starts from a new line and preserve internal indentation
            original_text = code_block.get_text()
            code_block.string = '\n' + original_text + '\n'

    # Convert the modified soup back to a string
    html_content = str(soup)

    # Convert plain URLs to markdown links outside of code blocks and HTML tags
    html_content = convert_urls_to_links(html_content)

    # Parse the modified HTML content with BeautifulSoup again to ensure proper formatting
    soup = BeautifulSoup(html_content, 'html.parser')

    # Write the final HTML content to a new file
    with open(output_file, 'w') as file:
        file.write(soup.prettify())

    print(f"Conversion complete. The HTML content has been saved to {output_file}")

# Run the main script
if __name__ == "__main__":
    main()