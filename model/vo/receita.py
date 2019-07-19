
class Receita:

    def __init__(self, municipio_codigo, receita_classificacao_codigo, receita_funcao_codigo, valor, ano):
        self.municipio_codigo = municipio_codigo
        self.receita_classificacao_codigo = receita_classificacao_codigo
        self.receita_funcao_codigo = receita_funcao_codigo
        self.valor = valor
        self.ano = ano

    def __repr__(self):
        return str(self.__dict__)