class MunicipioDAO:

    def insert(self, municipio, banco):
        mycursor = banco.cursor()
        sql = "INSERT INTO municipio (codigo, nome, uf, regiao) VALUES (%s, %s, %s, %s)"
        vals = (municipio.codigo, municipio.nome, municipio.uf, municipio.regiao)
        mycursor.execute(sql, vals)
        banco.commit()