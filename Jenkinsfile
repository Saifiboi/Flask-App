pipeline {
    agent any
    
    environment {
        API_KEY = credentials('b26c0a0e-e1d4-47a5-8704-5302bdffb2ff')
    }
    
    stages {
        stage('Test Credentials') {
            steps {
                script {
                    echo "Using secured credentials"
                    // Credential will be masked in logs
                    echo "API Key is securely loaded"
                }
            }
        }
        
    }
}
