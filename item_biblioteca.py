from abc import ABC, abstractmethod
class Itembiblioteca(ABC):
    def __init__(self, codigo, titulo, ano, disponivel):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = disponivel

    @abstractmethod
    def exibir_detalhes(self):
        pass

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def get_ano(self):
        return self.__ano
    
    def set_ano(self, valor):
        if valor > 0:
            self.__ano = valor
        else:
            raise ValueError("Ano inválido!")