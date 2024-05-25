#classe base

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf

    def cumprimentar(self):
        print(f'Olá ! Tudo bem? Me chamo {self.nome}')

    def setCpf(self, novoCpf):
        self.__cpf = novoCpf

    def getCpf(self):
        return self.__cpf 


# criação classe mãe que herda atributos e métodos da classe Pessoa

class Mae(Pessoa):
    def __init__(self, nome, cpf, corPele):
        super().__init__(nome, cpf)
        self.corPele = corPele

    def dancar(self):
        print(f'{self.nome} está dançando')


mae1 = Mae('Rosilene', '222.333.444-55', 'parda')
print(mae1.getCpf())

