#!/bin/bash

# Define the URL to the GitHub repository and the files to download
REPO_URL="https://raw.githubusercontent.com/arpansahu/common_readme/main"
FILES=("requirements.txt" "convert_readme_to_html.py")

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

# Function to download files
download_files() {
    for file in "${FILES[@]}"; do
        curl -O "$REPO_URL/readme_manager_html_detailed/$file"
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

# Run convert_readme_to_html.py
run_readme_to_html_generator() {
    python convert_readme_to_html.py
}

# Copy readme.html to the cloned repository
copy_readme_to_repo() {
    local repo_dir="arpansahu.me"
    cp readme.html "$repo_dir/templates/modules/project_detailed/project_partials/great_chat/"
}

# Deactivate and delete the environment
cleanup_env() {
    deactivate
    rm -rf env
}

# Delete downloaded files
delete_downloaded_files() {
    for file in "${FILES[@]}"; do
        rm -f "$file"
    done
}

# Clone repository with retry logic
clone_repo() {
    local repo_url="https://github.com/arpansahu/arpansahu.me"
    local repo_name=$(basename -s .git "$repo_url")
    local clone_success=false

    # Extract repository path from URL
    REPO_PATH="${repo_url#https://github.com/}"

    # Construct the authenticated URL for prod, plain URL for local
    if [ "$ENVIRONMENT" != "local" ]; then
        AUTHENTICATED_URL="https://${GIT_USERNAME}@github.com/${REPO_PATH}"
    else
        AUTHENTICATED_URL="https://github.com/${REPO_PATH}"
    fi

    # Log the URL being used (without exposing the password)
    echo "Using URL: $AUTHENTICATED_URL"

    # Retry logic for cloning
    for attempt in {1..3}; do
        echo "Attempt $attempt: Cloning repository: $AUTHENTICATED_URL"
        if GIT_TRACE_PACKET=1 GIT_TRACE=1 GIT_CURL_VERBOSE=1 git clone "$AUTHENTICATED_URL"; then
            echo "Successfully cloned repository: $repo_url"
            clone_success=true
            break
        else
            echo "Failed to clone repository: $repo_url (Attempt $attempt)"
        fi
    done

    if [ "$clone_success" = false ]; then
        echo "Failed to clone repository after 3 attempts"
        exit 1
    fi
}

# Check for changes and push if found
check_and_push_changes() {
    local repo_dir="arpansahu.me"
    cd "$repo_dir"

    git add .

    if ! git diff-index --quiet HEAD --; then
        echo "Changes detected, committing and pushing..."
        git commit -m "Update readme.html"
        git pull --rebase
        git push
    else
        echo "No changes detected."
    fi

    cd ..
}

# Delete cloned repository and generated files
final_cleanup() {
    rm -rf arpansahu.me
    rm -f readme.html Readme_converted.md
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
    run_readme_to_html_generator

    cleanup_env
    delete_downloaded_files

    # Clone the repository before copying the file
    clone_repo

    # Copy readme.html to the cloned repository
    copy_readme_to_repo

    # Check for changes and push if any
    check_and_push_changes

    # Final cleanup
    final_cleanup
}

# Execute the main function with provided arguments or default to prod environment
main "$@"