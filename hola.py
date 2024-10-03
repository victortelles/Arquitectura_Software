class Calculadora:
    # Constructor
    def __init__(self):
        pass

    # Método para sumar dos números
    def sumar(self, a, b):
        return a + b

    # Método para restar dos números
    def restar(self, a, b):
        return a - b

    # Método para multiplicar dos números
    def multiplicar(self, a, b):
        return a * b

    # Método para dividir dos números
    def dividir(self, a, b):
        if b == 0:
            return "Error: No se puede dividir por cero"
        return a / b


# Ejemplo de uso
calc = Calculadora()
print(f"Suma: {calc.sumar(10, 5)}")
print(f"Resta: {calc.restar(10, 5)}")
print(f"Multiplicación: {calc.multiplicar(10, 5)}")
print(f"División: {calc.dividir(10, 5)}")
