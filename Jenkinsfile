pipeline {
    agent any

    tools {
        allure 'allure'
    }

    stages {

        stage('Run tests') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                    dir('/var/jenkins_home/workspace/test31') {
                        sh """
                        python3 -m pip install -r requirements.txt --break-system-packages
                        python3 -m pytest . -m ${scope} --alluredir allure-results -v
                        """
                    }
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                dir('/var/jenkins_home/workspace/test31') {
                    sh 'allure generate allure-results -o allure-report --clean'
                }
            }
        }

        stage('Publish Report') {
            steps {
                dir('/var/jenkins_home/workspace/test31') {
                    allure([ results: [[path: 'allure-results']] ])
                }
            }
        }
    }

    post {
        always {
            dir('/var/jenkins_home/workspace/test31') {
                archiveArtifacts artifacts: 'allure-report/**/*', allowEmptyArchive: true
            }
        }
    }
}