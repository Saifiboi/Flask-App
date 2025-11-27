pipeline {
    agent any
    
    environment {
        API_KEY = credentials('api-key')
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
