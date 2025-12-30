pipeline {
    agent any
    
    environment {
        API_KEY = credentials('b26c0a0e-e1d4-47a5-8704-5302bdffb2ff')
        APP_VERSION = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "Checking out code from repository"
                    checkout scm
                }
            }
        }
        
        stage('Setup Environment') {
            steps {
                script {
                    echo "Setting up Python environment"
                    // Install dependencies
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    echo "Running pytest tests"
                    // Run pytest with verbose output and generate XML report
                    bat 'pytest test_app.py -v --junitxml=test-results.xml'
                }
            }
        }
        
        stage('Build Application') {
            steps {
                script {
                    echo "Building Flask application - Version ${APP_VERSION}"
                    // Create build directory
                    bat '''
                        if not exist "build" mkdir build
                        echo Build version: %APP_VERSION% > build\\version.txt
                    '''
                    
                    // Copy application files to build directory
                    bat '''
                        xcopy /E /I /Y app.py build\\
                        xcopy /E /I /Y templates build\\templates
                        xcopy /E /I /Y requirements.txt build\\
                    '''
                    
                    echo "Application packaged successfully"
                }
            }
        }
        
        stage('Create Artifact') {
            steps {
                script {
                    echo "Creating deployment artifact"
                    // Archive the build
                    bat '''
                        powershell Compress-Archive -Path build\\* -DestinationPath Flask-App-v%APP_VERSION%.zip -Force
                    '''
                    echo "Artifact created: Flask-App-v${APP_VERSION}.zip"
                }
            }
        }
        
        stage('Test Credentials') {
            steps {
                script {
                    echo "Using secured credentials"
                    // Credential will be masked in logs
                    echo "API Key is securely loaded"
                }
            }
        }
        
        stage('Prepare Deployment') {
            steps {
                script {
                    echo "Preparing for deployment"
                    echo "Artifact ready for deployment: Flask-App-v${APP_VERSION}.zip"
                    // You can add deployment commands here
                    // Example: Deploy to server, upload to cloud storage, etc.
                }
            }
        }
    }
    
    post {
        always {
            // Archive test results
            junit 'test-results.xml'
            
            // Archive build artifacts
            archiveArtifacts artifacts: 'Flask-App-v*.zip', fingerprint: true
            
            // Clean up build directory
            script {
                bat 'if exist build rmdir /S /Q build'
            }
        }
        success {
            echo 'Build and tests passed successfully!'
            echo "Deployment artifact: Flask-App-v${APP_VERSION}.zip is ready"
        }
        failure {
            echo 'Build or tests failed. Please check the results.'
        }
    }
}
