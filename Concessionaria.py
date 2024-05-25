#veículo
class Veiculo:
    def __init__(self, marca, modelo, anoFabricaco, preco):
        ''' Cria um objeto veículo com caractisticas generalistas'''
        self.marca = marca
        self.modelo = modelo
        self.anoFabricacao = anoFabricaco  
        self. preco = preco
    
    def exibirInformacoes(self):
        '''Exibi informacoes do veículo'''
        print (f'O veículo da {self. marca}, ano {self.anoFabricacao}, modelo {self.modelo} custa {self.preco}')

#carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, anoFabricaco, preco, nPortas,tipoCombustivel ):
        super().__init__(marca, modelo, anoFabricaco, preco)
        self.nPortas = nPortas
        self.tipoCombustivel = tipoCombustivel

#moto
class Moto(Veiculo):
    def __init__(self, marca, modelo, anoFabricaco, preco, cilindradas, partida):
        super().__init__(marca, modelo, anoFabricaco, preco)
        self.cilindradas = cilindradas
        self.partida = partida

#concessionaria

class Concessionaria:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.__listaVeiculos = []

    def adicionarVeiculo(self, veiculo):
        self.__listaVeiculos.append(veiculo)
        print('veiculo adicionado')

    def listarTodosVeiculos(self):
        for veiculo in self.__listaVeiculos:
            veiculo.exibirInformacoes()


DieguinhoCar = Concessionaria('Dieguinho Carros', 'Rua do Cheiro do Queijo Gorgonzola')

carro1 = Carro('Honda', 'Civic', 2024, 160000.50, 5, 'flex')
carro1.exibirInformacoes()

DieguinhoCar.adicionarVeiculo(carro1)

DieguinhoCar.__listaVeiculos