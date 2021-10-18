
pipeline {
    agent any
    
    environment {
        //HOME = "${env.WORKSPACE}"
        imageName = "finage/python_build"
        dockerImage = "${imageName}:${version}"
    }

    stages {
        /*stage('Pull branch') {
            steps {
                git branch: "master", url: 'https://github.com/finage/realpython_reader'
            }
        }*/
        stage('image build'){
            steps {
                script {
                    dockerImage = docker.build ("${imageName}:${version}", "--build-arg version=$version --build-arg package_name=$PACKAGE_NAME .")
                } 
            }
        }
        stage('deploy image') {
            steps{
                script {
                    docker.withRegistry('', 'docker_hub') {
                        dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }
  
    post {
        success {
            echo "${env.BUILD_URL} has result success"
        }
        failure {
            echo "${env.BUILD_URL} has result fail"
        }
        always {
            echo "Cleaning working directory..."
            cleanWs()   
        }
    }
}
