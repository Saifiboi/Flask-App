pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo "Checking out code"
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo "Installing dependencies"
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo "Running tests"
                bat 'pytest test_app.py -v'
            }
        }
        
        stage('Build') {
            steps {
                echo "Building application"
                bat 'if not exist "build" mkdir build'
                bat 'xcopy /Y app.py build\\'
                bat 'xcopy /E /I /Y templates build\\templates'
                bat 'xcopy /Y requirements.txt build\\'
                echo "Build complete"
            }
        }
        
        stage('Deploy') {
            steps {
                echo "Deploying to C:\\Deployment\\Flask-App"
                bat 'if not exist "C:\\Deployment\\Flask-App" mkdir C:\\Deployment\\Flask-App'
                bat 'xcopy /E /I /Y build\\* C:\\Deployment\\Flask-App\\'
                echo "Deployment complete!"
            }
        }
    }
    
    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed."
        }
    }
}
