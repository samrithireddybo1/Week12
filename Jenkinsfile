pipeline {
    agent any
   
    stages {

        stage('Run Selenium Tests with pytest') {
            steps {
                    echo "Running Selenium Tests using pytest"

                    // Install Python dependencies
                    bat '"C:\\Users\\samri\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'


                    //  Start Flask app in background
                    bat 'start /B "C:\\Users\\samri\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'
                    bat '"C:\\Users\\samri\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest -v'


                    // Run tests using pytest
                    
                    bat '"C:\\Users\\samri\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t week12:v1 ."
            }
        }
        stage('Docker Login') {
            steps {
                  bat 'docker login -u samrithi -p Samrithi@1605'
                }
            }
        stage('push Docker Image to Docker Hub') {
            steps {
                echo "push Docker Image to Docker Hub"
                bat "docker tag week12:v1 samrithi/week12:v1"               
                    
                bat "docker push samrithi/week12:v1"
                
            }
        }
        stage('Deploy to Kubernetes') { 
            steps { 
                    // apply deployment & service 
                    bat 'kubectl apply -f deployment.yaml --validate=false' 
                    bat 'kubectl apply -f service.yaml' 
            } 
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
