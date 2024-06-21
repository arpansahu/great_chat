#!/bin/bash

# Define the URL to the GitHub repository and the files to download
REPO_URL="https://raw.githubusercontent.com/arpansahu/common_readme/main"
FILES=("requirements.txt" "update_readme.py" "baseREADME.md")

# Function to download files
download_files() {
    for file in "${FILES[@]}"; 
    do
        curl -O "$REPO_URL/$file"
    done
}

# Create and activate virtual environment
create_and_activate_env() {
    python3 -m venv env
    source env/bin/activate
}

# Install requirements
install_requirements() {
    pip install -r requirements.txt
}

# Run update_readme.py
run_update_readme() {
    python update_readme.py
}

# Deactivate and delete the environment
cleanup_env() {
    deactivate
    rm -rf env
}

# Main script execution
main() {
    download_files
    create_and_activate_env
    install_requirements
    run_update_readme
    cleanup_env
}

# Execute the main function
main