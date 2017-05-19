pipeline {
    agent {
        node {
            label 'master'
        }
    }
    triggers {
        pollSCM('*/5 * * * *')
    }
    stages {
        stage('Testing') {
            steps {
		# Set up
		source activate hug-env
		sh pytest --junitxml results.xml src/test_api.py
            }
        }
    }
