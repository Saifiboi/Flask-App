pipeline {
    agent any

    // Define environment variables
    environment {
        MY_TOOL_VERSION = '1.2.3'
        DEPLOY_ENV = 'staging'
    }

    stages {
        stage('Build') {
            steps {
                echo "Building using tool version ${env.MY_TOOL_VERSION}"
            }
        }

        stage('Test') {
            steps {
                echo "Running tests in environment: ${env.DEPLOY_ENV}"
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying to environment: ${env.DEPLOY_ENV}"
            }
        }
    }

    post {
        always {
            echo 'It runs evertime...'
        }
    }
}
