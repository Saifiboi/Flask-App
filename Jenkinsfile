pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo "Checking out code"
                checkout scm
            }
        }
        
        stage('Setup') {
            steps {
                echo "Installing dependencies"
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                echo "Running tests"
                bat 'pytest test_app.py -v --junitxml=test-results.xml'
            }
        }
        
        stage('Build') {
            steps {
                echo "Building application"
                bat '''
                    if not exist "build" mkdir build
                    xcopy /Y app.py build\\
                    xcopy /E /I /Y templates build\\templates
                    xcopy /Y requirements.txt build\\
                '''
                
                bat 'powershell Compress-Archive -Path build\\* -DestinationPath Flask-App-build.zip -Force'
                echo "Build complete: Flask-App-build.zip"
            }
        }
    }
    
    post {
        always {
            junit allowEmptyResults: true, testResults: 'test-results.xml'
            archiveArtifacts artifacts: '*.zip', allowEmptyArchive: true
        }
        success {
            echo 'Build successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
