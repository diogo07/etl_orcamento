
class ReceitaDAO:

    def insert(self, receita, banco):
        mycursor = banco.cursor()
        sql = "INSERT INTO receita (municipio_codigo, classificacao_receita_codigo, funcao_receita_codigo, valor, ano) VALUES (%s, %s, %s, %s, %s)"
        vals = (receita.municipio_codigo, receita.receita_classificacao_codigo, receita.receita_funcao_codigo, receita.valor, receita.ano)
        mycursor.execute(sql, vals)
        banco.commit()


    def insert_sql(self, sql, dados, banco):
        mycursor = banco.cursor()
        try:
            mycursor.executemany(sql, dados)
            banco.commit()
        except Exception as e:
            print("Erro: "+str(e))

