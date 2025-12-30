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
        
        stage('Deploy') {
            steps {
                echo "Deploying Flask application..."
                
                bat 'if not exist "C:\\Deployment\\Flask-App" mkdir C:\\Deployment\\Flask-App'
                
                bat 'xcopy /E /I /Y build\\* C:\\Deployment\\Flask-App\\'
                
                echo "Files deployed to C:\\Deployment\\Flask-App"
                echo "To run the app manually, navigate to C:\\Deployment\\Flask-App and run: python app.py"
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
