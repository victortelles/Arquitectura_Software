pipeline {
    agent any

    stages {
        stage('Sumar') {
            steps {
                script {
                    sh 'python3 -c "a=10; b=5; print(f\'Resultado de la suma: {a + b}\')"'
                }
            }
        }
        stage('Restar') {
            steps {
                script {
                    sh 'python3 -c "a=10; b=5; print(f\'Resultado de la resta: {a - b}\')"'
                }
            }
        }
        stage('Multiplicar') {
            steps {
                script {
                    sh 'python3 -c "a=10; b=5; print(f\'Resultado de la multiplicación: {a * b}\')"'
                }
            }
        }
        stage('Dividir') {
            steps {
                script {
                    sh 'python3 -c "a=10; b=5; print(f\'Resultado de la división: {a / b if b != 0 else \'Error: No se puede dividir por cero\'}")"'
                }
            }
        }
    }
}
