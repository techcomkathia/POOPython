#livro tem Titulo, autor , ano, status
class Livro:
    def __init__(self, titulo: str, autor:str, ano:int, status:str) :
        ''' Cria um objeto da classe Livro com os atributos solicitados. O status deve ser "disponível" ou "indisponível"'''
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status

    def setDisponivel(self):
        self.status = 'disponível'

    def setIndisponivel(self):
        self.status = 'indisponível'

class Biblioteca:
    def __init__(self) :
        '''Cria um objeto da classe biblioteca, para agrupar objetos da classe livros. Contará com os métodos listar e adicionar livro'''
        self.__lista=[]

    def adicionarLivro(self, objetoLivro):
        self.__lista.append(objetoLivro)
        return 'O livro foi adicionado'

    def listarLivros(self):
        for livro in self.__lista:
            print(f'titulo : {livro.titulo}| ano: {livro.ano}| autor: {livro.autor}| disponibilidade: {livro.status}')


    def emprestarLivro(self, tituloLivro):
        #laço de repetição para percorrer toda a lista
        for livro in self.__lista:
            if livro.titulo == tituloLivro:
                livro.setIndisponivel()
                print(f'O Livro {livro.titulo} foi emprestado com sucesso. O seu status agora é indisponível')


livro1 = Livro('Título 1', 'Autor 1', '2001', 'disponível')
livro2 = Livro('Título 2', 'Autor 2', '2002', 'indisponível')
livro3 = Livro('Título 3', 'Autor 3', '2003', 'disponível')

minhaBiblioteca = Biblioteca()
minhaBiblioteca.adicionarLivro(livro1)
minhaBiblioteca.adicionarLivro(livro2)
minhaBiblioteca.adicionarLivro(livro3)
minhaBiblioteca.listarLivros()
minhaBiblioteca.emprestarLivro('Título 3')
minhaBiblioteca.listarLivros()







