#  Crie uma classe chamada ContaBancaria que represente uma conta bancária.
# A classe deve ter os atributos saldo e titular. Implemente métodos para depositar, sacar e verificar o saldo da conta. 

class ContaBancaria:
    def __init__(self,  titular: str, saldo:float=0):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valorDepositado:float):
        self.__saldo = self.saldo + valorDepositado

    def sacar(self, valorSacado):
        self.__saldo = self.saldo - valorSacado

    def consultarSaldo(self):
        ''' Retorna um texto com o titular da conta e o valor'''
        return( f'A conta do titular {self.titular} tem R$ {self.__saldo}')

contaJoao = ContaBancaria('Joao Vicente')
# print(contaJoao.consultarSaldo())


print(contaJoao.consultarSaldo())

