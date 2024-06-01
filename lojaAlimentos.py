# classe base

class Produto:
    def __init__(self, nome: str, cod: int, valor: float, qtd: int):
        self.__nome = nome
        self.__cod = cod
        self.__valor = valor
        self.__qtd = qtd

    def exibirInfo(self):
        return (f'Nome: {self.__nome} | Código: {self.__cod} | Valor: R${self.__valor} | Quantidade: {self.__qtd}')

    def adicionar(self, qtd: int = 1):
        self.__qtd += qtd

    def remover(self, qtd: int = 1):
        self.__qtd -= qtd


class Alimento(Produto):
    def __init__(self, nome, cod, valor, qtd, validade, peso):
        super().__init__(nome,cod,valor,qtd)
        self.__validade = validade
        self.__peso = peso

    def exibirInfo(self):
        return (f'Nome: {self.__nome} | Código: {self.__cod} | Valor: R${self.__valor} | Quantidade: {self.__qtd} | Peso(unitário): {self.__peso} | Validade: {self.__validade}')


class Bebida(Produto):
    def __init__(self, nome:str, cod:int, valor: float, qtd: int, alcoolica: bool, ml: int):
        '''Cria um objeto da classe Bebida. Deverá ser passado um booleano para o atributo alcoolica. True indica que é uma bebida alcoolica e False indica que não é.'''
        super().__init__(nome,cod,valor,qtd)
        self.__alcoolica = alcoolica
        self.__ml = ml

    def exibirInfo(self):
        return (f'Nome: {self.__nome} | Código: {self.__cod} | Valor: R${self.__valor} | Quantidade: {self.__qtd} | Peso(unitário): {self.__peso} | Validade: {self.__validade}')


class Estoque:
