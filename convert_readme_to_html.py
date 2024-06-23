import markdown
import re
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions.extra import ExtraExtension
from bs4 import BeautifulSoup

# Read the contents of the Readme.md file
with open('docker_converted.md', 'r') as file:
    readme_text = file.read()

# Convert plain URLs to markdown links outside of code blocks and HTML tags
def convert_urls_to_links(text):
    def replace(match):
        url = match.group(0)
        return f'<{url}>'
    
    # Pattern to identify URLs outside of code blocks and HTML tags
    url_pattern = re.compile(r'(?<![`">])(https?://[^\s`"<]+)(?![<`])')
    return url_pattern.sub(replace, text)

# Preprocess the markdown content to convert URLs to links outside of code blocks and HTML tags
readme_text = convert_urls_to_links(readme_text)

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

# Write the HTML content to a new file
with open('docker.html', 'w') as file:
    file.write(soup.prettify())

print("Conversion complete. The HTML content has been saved to Readme.html")