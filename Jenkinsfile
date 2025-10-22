
pipeline {
    agent any

    environment {
        // Replace this with your actual Python path from `where python`
        PYTHON_EXE = 'C:\\Users\\samri\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Run Selenium Tests with pytest') {
            steps {
                echo "Running Selenium Tests using pytest"

                // Use full Python path everywhere
                bat "${env.PYTHON_EXE} -m pip install --upgrade pip"
                bat "${env.PYTHON_EXE} -m pip install -r requirements.txt"

                // Start your Flask/Django/other app (background)
                bat "start /B ${env.PYTHON_EXE} app.py"
                bat 'ping 127.0.0.1 -n 5 > nul'

                // Run pytest
                bat "${env.PYTHON_EXE} -m pytest -v"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image"
                bat "docker build -t samrithi/week12:latest ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging in to Docker Hub"
                bat 'docker login -u samrithi -p Samrithi@1605'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker Image"
                bat "docker push samrithi/week12:latest"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes"
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check the logs.'
        }
    }
}

