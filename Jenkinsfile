
pipeline {
    agent any
    stages {

         stage('Checkout') {
            steps {
                script {
                    git url: 'https://github.com/GidSamina/Project_World_of_Games.git'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build('my_image_class10:latest')
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    docker.image('my_image_class10:latest').run('-p 8777:8777 -v $WORKSPACE/Scores.txt:/app/Scores.txt')
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
                    sh 'docker stop $(docker ps -q --filter ancestor=my_image_class10:latest)'
                    docker.withRegistry('https://index.docker.io/v1/') {
                        docker.image('my_image_class10:latest').push('latest')
                    }
                }
            }
        }
    }
}