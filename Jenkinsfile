def image
pipeline {
    environment {
        registry = "manish754/pipepline"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
    agent any

    stages{
        
        stage("Build Image") {

            steps {
                script {
                     image = registry + ":${env.BUILD_NUMBER}"
                     println ("${image}")
                     dockerImage = docker.build image
                    
                }
            }

        

        }

        stage("Testing - running in Jenkins Node") {

            steps {
                sh "docker run -d --name ${JOB_NAME} -p 5000:5000 ${image}"
            }
        }
        stage('Cleaning up') {
             steps {
                 sh "docker rm -f ${JOB_NAME}"
               }
        }
        stage("Push to Dockerhub") {
            steps {
                script {
                    docker.withRegistry('', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
       stage("running in staging")
            def remote = [:]
            remote.name = “ubuntu
            remote.host = "3.144.212.131"
            remote.allowAnyHosts = true
        
    withCredentials([sshUserPrivateKey(credentialsId: 'sshUser', keyFileVariable: 'identity', passphraseVariable: '', usernameVariable: 'ubuntu')]) {
             remote.user = ubuntu
             remote.identityFile = identity
             stage("SSH Steps Rocks!") {
             //sshCommand remote: remote, command: ‘docker pull ${image}’
              writeFile file: 'abc.sh', text: 'date'
              sshPut remote: remote, from: 'abc.sh', into: '.'
              }
            }
           }
       }   
    #}
 
 }
