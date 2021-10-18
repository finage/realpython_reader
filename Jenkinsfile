pipeline {
    agent { 
    //  dockerfile true
       docker {image 'python_package_build'}
    }
    
    environment {
        HOME = "${env.WORKSPACE}"
    }

    stages {
        stage('Install') {
            steps {
                echo "Installing package..."
                //sh "python3 -m pip install --upgrade pip"
                sh "python3 -m pip install -i https://test.pypi.org/simple/ '$PACKAGE_NAME'==1.0.'$BUILD_NUMBER'"
            }
        }
    }
  
    post {
        success {
            echo "${env.BUILD_URL} has result success"
            echo "Cleaning working directory..."
            cleanWs()
        }
        failure {
            echo "${env.BUILD_URL} has result fail"
            echo "Cleaning working directory..."
            cleanWs()
        }
    }
}
