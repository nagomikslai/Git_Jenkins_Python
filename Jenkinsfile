pipeline {
    agent any
    
    stages {
        stage('Display Branch Name') {
            steps {
                script {
                    def branchName = ''
                    // Retrieve the branch name
                    if (env.BRANCH_NAME == 'main') {
                        branchName = 'main'
                    } else if (env.BRANCH_NAME == 'dev-feature2') {
                        branchName = 'dev-feature2'
                    } else if (env.BRANCH_NAME == 'qa-feature1') {
                        branchName = 'qa-feature1'
                    } else {
                        branchName = 'Unknown Branch'
                    }
                    // Display the branch name
                    echo "Current Branch: ${branchName}"
                }
            }
        }
    }
}
