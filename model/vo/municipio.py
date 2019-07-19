
class Municipio:
    def __init__(self, codigo, nome, uf, regiao):
        self.codigo = codigo
        self.nome = nome
        self.uf = uf
        self. regiao = regiao


    def __repr__(self):
        return str(self.__dict__)