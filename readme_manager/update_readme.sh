#!/bin/bash

# Define the URL to the GitHub repository and the files to download
REPO_URL="https://raw.githubusercontent.com/arpansahu/common_readme/main"
FILES=("requirements.txt" "readme_updater.py" "baseREADME.md")

# Function to download files
download_files() {
    for file in "${FILES[@]}"; 
    do
        curl -O "$REPO_URL/$file"
        # Check if the file was downloaded successfully
        if [[ $? -ne 0 ]]; then
            echo "Error: Failed to download $file"
            exit 1
        fi
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

# Run readme_updater.py
run_readme_updater() {
    python readme_updater.py
}

# Deactivate and delete the environment
cleanup_env() {
    deactivate
    rm -rf env
}

# Delete downloaded files
delete_downloaded_files() {
    for file in "${FILES[@]}"; 
    do
        rm -f "$file"
    done
}

# Function to set up the environment
setup_environment() {
    if [ "$ENVIRONMENT" != "local" ]; then
        # Path to the GIT_ASKPASS helper script
        GIT_ASKPASS_HELPER="$(pwd)/git-askpass.sh"

        # Create the GIT_ASKPASS helper script
        echo "Creating GIT_ASKPASS helper script"
        echo '#!/bin/sh' > "$GIT_ASKPASS_HELPER"
        echo 'echo $GIT_PASSWORD' >> "$GIT_ASKPASS_HELPER"
        chmod +x "$GIT_ASKPASS_HELPER"

        # Export GIT_ASKPASS
        export GIT_ASKPASS="$GIT_ASKPASS_HELPER"
    fi
}

# Function to check for changes, commit, and push
check_and_commit_changes() {
    git add .
    if git diff-index --quiet HEAD; then
        echo "No changes to commit"
    else
        git commit -m "Automated update of README"
        git pull --rebase
        git push
    fi
}

# Main script execution
main() {
    # Change to the directory where the script is located
    cd "$(dirname "$0")"
    
    # Determine the environment
    ENVIRONMENT=${1:-prod}
    
    setup_environment
    download_files
    create_and_activate_env
    install_requirements
    run_readme_updater
    check_and_commit_changes
    cleanup_env
    delete_downloaded_files
}

# Execute the main function
main "$@"