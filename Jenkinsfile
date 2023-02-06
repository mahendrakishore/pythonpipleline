pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        bat 'git branch: \'main\', credentialsId: \'944c604f-a8aa-4ff0-948d-7b8bbd0a91ae\', url: \'https://github.com/mahendrakishore/pythonpipleline.git\''
      }
    }

  }
}