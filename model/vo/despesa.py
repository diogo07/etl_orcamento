
class Despesa:

    def __init__(self, municipio_codigo, despesa_classificacao_codigo, despesa_funcao_codigo, valor, ano):
        self.municipio_codigo = municipio_codigo
        self.despesa_classificacao_codigo = despesa_classificacao_codigo
        self.despesa_funcao_codigo = despesa_funcao_codigo
        self.valor = valor
        self.ano = ano

    def __repr__(self):
        return str(self.__dict__)