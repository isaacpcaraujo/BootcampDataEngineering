class Calculadora:
    def __init__(self, num1, num2):
        self.valorA = num1
        self.valorB = num2

    def soma(self):
        return self.valorA + self.valorB

    def sub(self):
        return self.valorA - self.valorB

    def mult(self):
        return self.valorA * self.valorB

    def div(self):
        return self.valorA / self.valorB

if __name__ == "__main__":
    a = float(input("Digite o primeiro numero: "))
    b = float(input("Digite o segundo numero: "))

    calculadora = Calculadora(a,b)
    print(calculadora.valorA)
    print(calculadora.valorB)
    print('Soma =', calculadora.soma())
    print('Subtração =', calculadora.sub())
    print('Multiplicação =', calculadora.mult())
    print('Divisão =', calculadora.div())
