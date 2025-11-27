pipeline {
    agent any

    tools {
        // Use the Maven tool configured in Jenkins
        maven 'Maven-3.9.2' // Replace with your Maven tool name in Jenkins
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building project with Maven...'
                // Windows users should use 'bat' instead of 'sh'
                bat 'mvn clean install'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Windows: replace any sh command with bat
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying project...'
            }
        }
    }

    post {
        always {
            echo 'Cleaning workspace...'
        }
    }
}
