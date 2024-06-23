import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.nl2br import Nl2BrExtension
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

# Function to extract code blocks from the intermediate file
def extract_code_blocks(intermediate_file):
    with open(intermediate_file, 'r') as file:
        lines = file.readlines()
    
    code_blocks = []
    inside_code_block = False
    current_block = []

    for line in lines:
        if line.lstrip().startswith("```"):
            if inside_code_block:
                code_blocks.append("\n".join(current_block))
                current_block = []
            inside_code_block = not inside_code_block
        elif inside_code_block:
            current_block.append(line.rstrip("\n"))
    
    return code_blocks

# Function to process the markdown content and convert it to HTML
def process_markdown_to_html(input_file, intermediate_file, output_file):
    # Adjust code blocks
    adjust_code_blocks(input_file, intermediate_file)
    
    # Read the adjusted markdown file
    with open(intermediate_file, 'r') as file:
        readme_text = file.read()
    
    # Extract original code blocks
    original_code_blocks = extract_code_blocks(intermediate_file)
    
    # Convert markdown to HTML with preserved code blocks, <br> tags for line breaks, and URL handling
    html_content = markdown.markdown(readme_text, extensions=[FencedCodeExtension(), Nl2BrExtension(), ExtraExtension()])
    
    # Parse the HTML content with BeautifulSoup to ensure no alteration to existing HTML tags and attributes
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Replace code blocks with the original content, ensuring they start and end on new lines with proper indentation
    code_block_index = 0
    for pre in soup.find_all('pre'):
        if pre.code:
            code_block = pre.code
            if code_block_index < len(original_code_blocks):
                original_code = '\n' + original_code_blocks[code_block_index] + '\n'
                code_block.string = original_code
                code_block_index += 1
    
    # Write the final HTML content to a new file
    with open(output_file, 'w') as file:
        file.write(soup.prettify(formatter=None))

    print(f"Conversion complete. The HTML content has been saved to {output_file}")

# Example usage
input_file = 'Readme.md'
intermediate_file = 'Readme_converted.md'
output_file = 'Readme.html'
process_markdown_to_html(input_file, intermediate_file, output_file)