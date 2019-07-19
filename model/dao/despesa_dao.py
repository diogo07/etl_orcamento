
class DespesaDAO:

    def insert(self, despesa, banco):
        mycursor = banco.cursor()
        sql = "INSERT INTO despesa (municipio_codigo, classificacao_despesa_codigo, funcao_despesa_codigo, valor, ano) VALUES (%s, %s, %s, %s, %s)"
        vals = (despesa.municipio_codigo, despesa.despesa_classificacao_codigo, despesa.despesa_funcao_codigo, despesa.valor, despesa.ano)
        mycursor.execute(sql, vals)
        banco.commit()


    def insert_sql(self, sql, dados, banco):
        mycursor = banco.cursor()
        try:
            mycursor.executemany(sql, dados)
            banco.commit()
        except Exception as e:
            print("Erro: "+e)

