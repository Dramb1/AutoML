pipeline {
    agent any

    stages {
        stage('git') {
            steps {
                git branch: 'main', url:'https://github.com/Dramb1/AutoML.git'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('data_creation'){
            steps {
                sh 'python3 data_creation.py'
            }
        }
        stage('model_preprocessing'){
            steps {
                sh 'python3 model_preprocessing.py'
            }
        }
        stage('model_preparation'){
            steps {
                sh 'python3 model_preparation.py'
            }
        }
        stage('model_testing'){
            steps {
                sh 'python3 model_testing.py'
            }
        }
    }
}
