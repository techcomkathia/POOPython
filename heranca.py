#classe base

class Trouxa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf

    def cumprimentar(self):
        print(f'Olá ! Tudo bem? Me chamo {self.nome}')

    def setCpf(self, novoCpf):
        self.__cpf = novoCpf

    def getCpf(self):
        return self.__cpf 


class Bruxo:
    def __init__(self, casa, patrono) :
        self.casa = casa
        self.patrono = patrono

    def lancarFeitico(self):
        print('Lançou feitiço')


class Mestico(Trouxa, Bruxo):
    def __init__(self, nome, cpf, casa, patrono):
        super().__init__(nome, cpf)
        Bruxo.__init__(self, casa, patrono)


mestico1 = Mestico('Luna', '100.000.000-35','Grifinólia','coelho')

mestico1.lancarFeitico()