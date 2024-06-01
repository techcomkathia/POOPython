# classe base

class Produto:
    def __init__(self, nome: str, cod: int, valor: float, qtd: int):
        self.nome = nome
        self.cod = cod
        self.valor = valor
        self.qtd = qtd

    def exibirInfo(self):
        return (f'Nome: {self.nome} | Código: {self.cod} | Valor: R${self.valor} | Quantidade: {self.qtd}')

    def adicionar(self, qtd: int = 1):
        self.nome += qtd

    def remover(self, qtd: int = 1):
        self.qtd -= qtd


class Alimento(Produto):
    def __init__(self, nome, cod, valor, qtd, validade, peso):
        super().__init__(nome,cod,valor,qtd)
        self.__validade = validade
        self.__peso = peso

    def exibirInfo(self):
        return (f'Nome: {self.nome} | Código: {self.cod} | Valor: R${self.valor} | Quantidade: {self.qtd} | Peso(unitário): {self.__peso} | Validade: {self.__validade}')


class Bebida(Produto):
    def __init__(self, nome:str, cod:int, valor: float, qtd: int, alcoolica: bool, ml: int):
        '''Cria um objeto da classe Bebida. Deverá ser passado um booleano para o atributo alcoolica. True indica que é uma bebida alcoolica e False indica que não é.'''
        super().__init__(nome,cod,valor,qtd)
        self.__alcoolica = alcoolica
        self.__ml = ml

    def exibirInfo(self):
        return (f'Nome: {self.nome} | Código: {self.cod} | Valor: R${self.valor} | Quantidade: {self.qtd} | ML(unitário): {self.__ml} | Alcoolica: {self.__alcoolica}')


class Estoque:
    def __init__(self, listaProdutos = []):
       self.__listaProdutos = listaProdutos

    def adicionar(self, produto):
        self.__listaProdutos.append(produto)

    def remover(self, codProduto):
        for produto in self.__listaProdutos:
            if codProduto == produto.cod:
                self.__listaProdutos.remove(produto)



    def exibirDisponivel(self):
        for produto in self.__listaProdutos:
            if produto.qtd >= 1:
                print(produto.exibirInfo())

    def exibirIndisponivel(self):
        for produto in self.__listaProdutos:
            if produto.qtd == 0:
                print(produto.exibirInfo())

    def exibirTodosProdutos(self):
        for produto in self.__listaProdutos:
           print(produto.exibirInfo())


bebida1 = Bebida('achocolatado',1,2.90,10,False,250)
alimento1= Alimento('arroz',2,5.90,50,'10/12/25','1kg')

estoque =Estoque()

estoque.adicionar(bebida1)
estoque.adicionar(alimento1)

estoque.exibirDisponivel()
print("-"*50)
bebida1.remover(10)
estoque.exibirIndisponivel()
estoque.remover(1)
print('*************************')
estoque.exibirTodosProdutos()

