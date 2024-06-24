pipeline {
    agent { label 'local' }
    stages {
        stage('Initialize') {
            steps {
                script {
                    // Log the current workspace path
                    echo "Current workspace path is: ${env.WORKSPACE}"
                    // Log the branch name
                    echo "Current branch is: ${env.GIT_BRANCH}"
                }
            }
        }
        stage('Checkout') {
            steps {
                // Checkout code from SCM
                checkout scm
            }
        }
        stage('Dependencies') {
            steps {
                script {
                    // Copy .env file to the workspace
                    sh "sudo cp /root/projectenvs/great_chat/.env ${env.WORKSPACE}/"
                }
            }
        }
        stage('Production') {
            when {
                expression {
                    // Collect all changed files
                    def changes = currentBuild.changeSets.collect { it.items.collect { it.affectedFiles.collect { it.path } } }.flatten()

                    // Define the file(s) to be excluded from triggering a deploy
                    def excludedFiles = ['Readme.md']

                    // Check if the only changed files are in the excluded list
                    def onlyExcludedFilesChanged = changes.every { changedFile -> 
                        excludedFiles.contains(changedFile)
                    }

                    // Proceed with deployment if not only excluded files are changed
                    return !onlyExcludedFilesChanged
                }
            }
            steps {
                script {
                    // Deploy using Docker Compose
                    sh "docker compose up --build --detach"
                    
                    // Set a flag to indicate deployment execution
                    currentBuild.description = 'DEPLOYMENT_EXECUTED'
                }
            }
        }
    }
    post {
        success {
            script {
                if (currentBuild.description == 'DEPLOYMENT_EXECUTED') {
                    // Send success notification email
                    sh """curl -s \
                    -X POST \
                    --user $MAIL_JET_API_KEY:$MAIL_JET_API_SECRET \
                    https://api.mailjet.com/v3.1/send \
                    -H "Content-Type:application/json" \
                    -d '{
                        "Messages":[
                                {
                                        "From": {
                                                "Email": "$MAIL_JET_EMAIL_ADDRESS",
                                                "Name": "ArpanSahuOne Jenkins Notification"
                                        },
                                        "To": [
                                                {
                                                        "Email": "$MY_EMAIL_ADDRESS",
                                                        "Name": "Development Team"
                                                }
                                        ],
                                        "Subject": "${currentBuild.fullDisplayName} deployed successfully",
                                        "TextPart": "Hola Development Team, your project ${currentBuild.fullDisplayName} is now deployed",
                                        "HTMLPart": "<h3>Hola Development Team, your project ${currentBuild.fullDisplayName} is now deployed </h3> <br> <p> Build Url: ${env.BUILD_URL}  </p>"
                                }
                        ]
                    }'"""

                    // List files in the workspace and in specific directories for debugging
                    sh "ls -l ${env.WORKSPACE}"
                    sh "ls -l ${env.WORKSPACE}/readme_manager"
                    sh "ls -l ${env.WORKSPACE}/readme_manager_html_detailed"

                    // Check out the branch before running the script
                    sh "git checkout ${env.GIT_BRANCH}"

                    // Trigger update_readme.sh and convert_readme_to_html.sh
                    if (fileExists("${env.WORKSPACE}/readme_manager/update_readme.sh")) {
                        sh "bash ${env.WORKSPACE}/readme_manager/update_readme.sh"
                    } else {
                        echo "update_readme.sh not found"
                    }
                    if (fileExists("${env.WORKSPACE}/readme_manager_html_detailed/convert_readme_to_html.sh")) {
                        sh "bash ${env.WORKSPACE}/readme_manager_html_detailed/convert_readme_to_html.sh"
                    } else {
                        echo "convert_readme_to_html.sh not found"
                    }
                }
            }
        }
        failure {
            script {
                // Send failure notification email
                sh """curl -s \
                -X POST \
                --user $MAIL_JET_API_KEY:$MAIL_JET_API_SECRET \
                https://api.mailjet.com/v3.1/send \
                -H "Content-Type:application/json" \
                -d '{
                    "Messages":[
                            {
                                    "From": {
                                            "Email": "$MAIL_JET_EMAIL_ADDRESS",
                                            "Name": "ArpanSahuOne Jenkins Notification"
                                    },
                                    "To": [
                                            {
                                                    "Email": "$MY_EMAIL_ADDRESS",
                                                    "Name": "Development Team"
                                            }
                                    ],
                                    "Subject": "${currentBuild.fullDisplayName} deployment failed",
                                    "TextPart": "Hola Development Team, your project ${currentBuild.fullDisplayName} deployment failed",
                                    "HTMLPart": "<h3>Hola Development Team, your project ${currentBuild.fullDisplayName} is not deployed, Build Failed </h3> <br> <p> Build Url: ${env.BUILD_URL}  </p>"
                            }
                    ]
                }'"""
            }
        }
    }
}