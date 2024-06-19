import requests

# Define the main README file
main_readme_file = "README.md"

# Define a dictionary with the placeholders and their corresponding GitHub raw URLs
include_files = {
    "README of Docker Installation": "https://raw.githubusercontent.com/arpansahu/common_readme/main/Docker%20Readme/docker_installation.md",
    "README of Nginx Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/nginx.md",
    "README of Jenkins Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Jenkins.md",
    "README of PostgreSql Server With Nginx Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Postgres.md",
    "README of PGAdmin4 Server With Nginx Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/PostgresUI.md",
    "README of Portainer Server With Nginx Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Portainer.md",
    "README of Redis Server Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Redis.md",
    "README of Redis Commander Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/RedisComander.md",
    "README of Minio Server Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Minio.md",
    "README of Intro": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Intro.md",
    "env.example": "https://raw.githubusercontent.com/arpansahu/great_chat/main/env.example",
    "docker-compose.yml": "https://github.com/arpansahu/great_chat/blob/main/docker-compose.yml",
    "Dockerfile": "https://github.com/arpansahu/great_chat/blob/main/Dockerfile",
}

# Read the main README file content
with open(main_readme_file, "r") as main_file:
    readme_content = main_file.read()

# Function to replace placeholders with actual file content from GitHub
def include_file_content_from_github(content, placeholder, file_url):
    try:
        response = requests.get(file_url)
        response.raise_for_status()
        included_content = response.text
        return content.replace(f"[{placeholder}]", included_content)
    except requests.RequestException as e:
        print(f"Error fetching {file_url}: {e}")
        return content

# Replace all placeholders with their corresponding file content from GitHub
for placeholder, file_url in include_files.items():
    readme_content = include_file_content_from_github(readme_content, placeholder, file_url)

# Write the updated content back to the main README file
with open(main_readme_file, "w") as main_file:
    main_file.write(readme_content)

print("README.md has been updated with the referenced content.")