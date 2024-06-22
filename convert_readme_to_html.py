import markdown
import re
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions.extra import ExtraExtension

# Read the contents of the Readme.md file
with open('Readme.md', 'r') as file:
    readme_text = file.read()

# Convert plain URLs to markdown links
def convert_urls_to_links(text):
    url_pattern = re.compile(r'(https?://[^\s]+)')
    return url_pattern.sub(r'<\1>', text)

# Preprocess the markdown content to convert URLs to links
readme_text = convert_urls_to_links(readme_text)

# Convert markdown to HTML with preserved code blocks, <br> tags for line breaks, and URL handling
html_content = markdown.markdown(readme_text, extensions=[FencedCodeExtension(), Nl2BrExtension(), ExtraExtension()])

# Write the HTML content to a new file
with open('Readme.html', 'w') as file:
    file.write(html_content)

print("Conversion complete. The HTML content has been saved to Readme.html")