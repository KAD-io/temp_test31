pipeline {
  agent any
  stages {
    stage('Run tests') {
      steps{
        script {
          sh 'cd /var/jenkins_home/workspace/test31'
        }
      steps{
        script {
          sh 'python3 -m pytest . -m unittests --alluredir allure-results'
        }
      steps{
        script {
          sh 'python3 -m pytest . -m unittests --alluredir allure-results'
        }
      }
    }
  }
}}}