class CalculadoraMCD_MCM:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcular_mcd(self):
        a = self.num1
        b = self.num2
        while b != 0:
            a, b = b, a % b
        return a

    def calcular_mcm(self):
        mcd = self.calcular_mcd()
        return (self.num1 * self.num2) // mcd

# Ejemplo de uso
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

calculadora = CalculadoraMCD_MCM(num1, num2)
print("El máximo común divisor de", num1, "y", num2, "es:", calculadora.calcular_mcd())
print("El mínimo común múltiplo de", num1, "y", num2, "es:", calculadora.calcular_mcm())