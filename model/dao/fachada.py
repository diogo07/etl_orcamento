import csv
from model.dao.conexao import Conexao
from model.vo.despesa import Despesa
from model.vo.receita import Receita
from model.dao.despesa_dao import DespesaDAO
from model.dao.receita_dao import ReceitaDAO
from model.dao.municipio_dao import MunicipioDAO
import json
from model.vo.municipio import Municipio
from utils.utils import Utils
import rota_raiz

class Fachada:

    def __init__(self):
        self.caminho = rota_raiz.get_caminho()

    def inserirDespesa(self, ano_inicio, ano_fim):
        for i in range(ano_inicio, ano_fim+1):
            print('INICIANDO PROCESSAMENTO DOS DADOS SOBRE DESPESAS DO ANO DE '+str(i)+' ...')
            utils = Utils()

            with open(str(self.caminho)+"/utils/dados/despesas/por função/DespesasporFuncao" + str(i) + ".csv", 'r', encoding='latin-1') as csv_file:
                    tempo_inicial = utils.get_hora()
                    arquivo = csv.reader(csv_file, delimiter=';')
                    c = Conexao()
                    conexao = c.conn_postgre('localhost', 'postgres', 'postgres', 'orcamento_publico')
                    despesaDao = DespesaDAO()

                    sql = "INSERT INTO despesa (municipio_codigo, classificacao_despesa_codigo, funcao_despesa_codigo, valor, ano) VALUES (%s,%s,%s,%s,%s)"
                    dados = []
                    total_linhas = 0
                    linhas_usadas = 0

                    for row in arquivo:
                        total_linhas += 1
                        if (utils.isnumber(row[5]) and str(row[5])[2] != '.') or (utils.isnumber(row[5]) == False):
                            linhas_usadas += 1
                            despesa = Despesa(row[1], utils.get_classificacao_despesa(row[4]),
                                              utils.get_funcao_despesa(row[5]), float(row[6].replace(",", ".")), i)
                            dados.append((despesa.municipio_codigo, despesa.despesa_classificacao_codigo,
                                          despesa.despesa_funcao_codigo, despesa.valor, str(despesa.ano)))

                    despesaDao.insert_sql(sql, dados, conexao)
                    tempo_final = utils.get_hora()
                    tempo_gasto = tempo_final - tempo_inicial
                    print("tempo gasto: " + str(tempo_gasto))

                    print('total linhas: '+str(total_linhas))
                    print('linhas usadas: ' + str(linhas_usadas))
                    print('\n')

    def inserirReceita(self, ano_inicio, ano_fim):
        for i in range(ano_inicio, ano_fim+1):
            print('INICIANDO PROCESSAMENTO DOS DADOS SOBRE RECEITAS DO ANO DE '+str(i)+' ...')
            utils = Utils()

            with open(str(self.caminho)+"/utils/dados/receitas/ReceitasOrcamentarias" + str(i) + ".csv", 'r', encoding='latin-1') as csv_file:
                    tempo_inicial = utils.get_hora()
                    arquivo = csv.reader(csv_file, delimiter=';')
                    c = Conexao()
                    conexao = c.conn_postgre('localhost', 'postgres', 'postgres', 'orcamento_publico')
                    receitaDao = ReceitaDAO()

                    sql = "INSERT INTO receita (municipio_codigo, classificacao_receita_codigo, funcao_receita_codigo, valor, ano) VALUES (%s,%s,%s,%s,%s)"
                    dados = []

                    total_linhas = 0
                    linhas_usadas = 0

                    for row in arquivo:
                        total_linhas += 1
                        if row[5] != 'Total Receitas' and str(row[5])[2] == '0':
                            linhas_usadas += 1
                            receita = Receita(row[1], utils.get_classificacao_receita(row[4]),
                                              utils.get_funcao_receita(row[5]), float(row[6].replace(",", ".")), i)
                            dados.append((receita.municipio_codigo, receita.receita_classificacao_codigo,
                                          receita.receita_funcao_codigo, receita.valor, str(receita.ano)))

                    receitaDao.insert_sql(sql, dados, conexao)
                    tempo_final = utils.get_hora()
                    tempo_gasto = tempo_final - tempo_inicial
                    print("tempo gasto: " + str(tempo_gasto))
                    print('total linhas: '+str(total_linhas))
                    print('linhas usadas: ' + str(linhas_usadas))
                    print('\n')

    def inserirMunicipios(self):
        with open(str(self.caminho)+"/utils/dados/municipios/municipios.json", "r",
                  encoding="utf8") as write_file:
            dados = json.load(write_file)
            for i in range(len(dados)):
                municipio = Municipio(dados[i]['id'], dados[i]['nome'],
                                      dados[i]['microrregiao']['mesorregiao']['UF']['sigla'],
                                      dados[i]['microrregiao']['mesorregiao']['UF']['regiao']['nome'])
                c = Conexao()
                conexao = c.conn_postgre('localhost', 'postgres', 'postgres', 'orcamento_publico')
                municipioDao = MunicipioDAO()
                municipioDao.insert(municipio, conexao)