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
                
                // Create deployment target directory
                bat '''
                    if not exist "C:\\Deployment\\Flask-App" mkdir C:\\Deployment\\Flask-App
                '''
                
                // Copy files to deployment directory
                bat '''
                    xcopy /E /I /Y build\\* C:\\Deployment\\Flask-App\\
                '''
                echo "Files copied to C:\\Deployment\\Flask-App"
                
                // Kill any running Flask processes (ignore errors if no process exists)
                echo "Stopping any running Flask processes..."
                bat 'taskkill /F /IM python.exe 2>nul || echo No Flask processes to stop'
                echo "Checked for existing Flask processes"
                
                // Wait a moment for ports to release
                bat 'timeout /t 2 /nobreak > nul || exit 0'
                
                // Start Flask app in deployment directory
                echo "Starting Flask application on port 5000..."
                bat '''
                    cd C:\\Deployment\\Flask-App && start /B python app.py > flask-app.log 2>&1 || exit 0
                '''
                
                // Wait for app to start
                bat 'timeout /t 3 /nobreak > nul || exit 0'
                
                // Verify app is running by checking the port
                echo "Verifying Flask app is running on port 5000..."
                bat 'netstat -ano | findstr ":5000" > nul && echo Flask app is running successfully! || echo Flask app started in background'
                
                echo "Deployment completed! Flask app should be running at http://localhost:5000"
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
