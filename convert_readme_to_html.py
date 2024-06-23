import markdown
import re
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.nl2br import Nl2BrExtension
from markdown.extensions.extra import ExtraExtension
from bs4 import BeautifulSoup

# Read the contents of the Readme.md file
with open('docker.md', 'r') as file:
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

# Ensure all <pre><code> tags are correctly formatted
for pre in soup.find_all('pre'):
    if pre.code:
        # Preserve class if already present
        if 'class' in pre.code.attrs:
            classes = pre.code.attrs['class']
        else:
            classes = []
        classes.append('language-bash')  # or other language as needed
        pre.code.attrs['class'] = classes

        # Add a newline before the content within <pre><code> blocks
        code_content = pre.code.string
        pre.code.string = '\n' + code_content.strip() + '\n'

# Write the HTML content to a new file
with open('docker.html', 'w') as file:
    file.write(soup.prettify())

print("Conversion complete. The HTML content has been saved to docker.html")