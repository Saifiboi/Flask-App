pipeline {
    agent any

    // Define parameters at the top level
    parameters {
        string(name: 'VERSION', defaultValue: '1.0.0', description: 'Specify the version')
        choice(name: 'VERSION', choices: ['1.1.0', '1.2.0', '1.3.0'], description: 'Choose a version')
        booleanParam(name: 'executeTests', defaultValue: true, description: 'Run the test stage?')
    }

    environment {
        MY_TOOL_VERSION = "${params.VERSION}"
    }

    stages {
        stage('Build') {
            steps {
                echo "Building project version ${env.MY_TOOL_VERSION}"
                bat "echo Building version ${env.MY_TOOL_VERSION}"
            }
        }

        stage('Test') {
            when {
                expression { return params.executeTests == true }
            }
            steps {
                echo "Running tests for version ${env.MY_TOOL_VERSION}"
                bat "echo Testing version ${env.MY_TOOL_VERSION}"
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying version ${env.MY_TOOL_VERSION}"
                bat "echo Deploying version ${env.MY_TOOL_VERSION}"
            }
        }
    }

    post {
        always {
            echo 'Cleaning workspace...'
            cleanWs()
        }
    }
}
