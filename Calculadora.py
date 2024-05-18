# 4 operações básicas

class Calculadora:
    def __init__(self):
        print('calculadora criada')
    
    def somar(self, num1, num2):
        return num1 + num2
    
    def subtrair(self, num1, num2):
        return num1 - num2
    
    def multiplicar(self, num1, num2):
        return num1 * num2
    
    def dividir(self, num1, num2):
        if (num2 == 0):
            return " divisão por 0 é impossível"
        else:
            return num1 / num2


calculadoraDaKathia = Calculadora()

print(calculadoraDaKathia.somar(2,2))