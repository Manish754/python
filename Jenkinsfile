pipeline{

    agent any

    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }
stages {
    stage('gitclone')

        step {
            git 'https://github.com/Manish754/python.git'
        }
}

stage('Build') {

    steps {
        sh 'docker build -t manish754/python:latest .'
    }
}

stage('Login') {
    steps {
        sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
    }
}
stage('Push') {
    step {
        sh 'docker push manish754/python:latest'

    }
}
post {
    always {
        sh 'docker logout'
    }
}
