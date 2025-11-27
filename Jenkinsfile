pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Example: bat 'pip install -r requirements.txt' for Windows
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                // Example: run tests
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Example: bat 'python app.py' or deploy script
            }
        }
    }

    post {
        always {
            echo 'This runs always, regardless of success or failure'
            // Example: cleanup workspace
            cleanWs()
        }

        failure {
            echo 'This runs only if the pipeline failed'
            // Example: send failure notification
        }
    }
}
