pipeline {
  agent any
  stages {
    stage('Run tests') {
      steps{
        script {
          sh 'cd /var/jenkins_home/workspace/test31'
          sh 'python3 -m pytest . -m unittests --alluredir allure-results'
          sh 'python3 -m pip install -r requirements.txt --break-system-packages'
        }
  }
}}}