#características : temperamento, tamanho, raça, cor, nome
# ações :  latir, pular, correr, comer

class Cachorro:
    def __init__(self, temperamento, tamanho, raca, cor, nome):
        self.nome = nome
        self.temperamento = temperamento
        self.tamanho = tamanho
        self.raca= raca
        self.cor= cor

    def latir(self):
        print( f'{self.nome} está latindo')

cachorro1 = Cachorro('dócil', 'pequeno', 'SRD', 'Preto e cinza', 'Nick')

cachorro1.latir()
print(cachorro1.nome)
cachorro1.nome= 'Cleitinho'
print(cachorro1.nome)