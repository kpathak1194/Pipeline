pipeline {
         agent any {
                 stages {
                     stage('One') {
                            steps { 
                                    echo 'Hi. This is kartik Pathak'
                                    }
                             }
                             stage('Two'){
                                      steps {
                                       input('Do you want tp Proceed?')
                                       }
                                 }
                                 stage('Three') {
                                        when {
                                             not {
                                                  branch "master"
                                                  }
                                             }
                                       steps  {
                                                echo "Hello"
                                                }
                                            }    
                                    stage('Four') {
                                                    parallel {
                                                              stage('Unit Test') {
                                                                                   steps {
                                                                                           echo "Running the unit test..."
                                                                                          }
                                                                           }
                                                                           stage('Integaration Testing") {
                                                                                                 agent {
                                                                                                         docker {
                                                                                                                  resuasable false
                                                                                                                  image 'ubuntu'
                                                                                                               }   
                                                                                                     }
                                                                                                     steps {
                                                                                                             echo 'Running the integration test...'
                                                                                                             }
                                                                                                        }
                                                                                                }
}
}
}
}
                                                                                                        
                                      
                                      
                                   
                         
