pipeline {
    agent { label 'local' }
    stages {
        stage('Initialize') {
            steps {
                script {
                    // Log the current workspace path
                    echo "Current workspace path is: ${env.WORKSPACE}"
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
                    // Trigger another Jenkins job
                    build job: 'common_readme', parameters: [string(name: 'project_git_url', value: 'https://github.com/arpansahu/great_chat'), string(name: 'environment', value: 'prod')], wait: false
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