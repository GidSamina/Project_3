
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    docker.build('your-image-name')
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image('my_image_class9:latest').run('-p 8777:8777 -v $WORKSPACE/Scores.txt:/app/Scores.txt')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'python e2e.py'
                }
            }
        }
        stage('Finalize') {
            steps {
                script {
                    sh 'docker stop $(docker ps -q --filter ancestor=my_image_class9:latest)'
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        docker.image('my_image_class9:latest').push('latest')
                    }
                }
            }
        }
    }
}
