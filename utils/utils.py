from datetime import datetime
import csv
class Utils:

    def contador_linhas(self, csv_file):
        arquivo = csv.reader(csv_file, delimiter=';')
        return  sum(1 for row in arquivo)


    def get_hora(self):
        return datetime.now()


    def get_classificacao_despesa(self, texto):
        if texto == 'Despesas Empenhadas':
            return 1
        elif texto == 'Despesas Liquidadas':
            return 2
        elif texto == 'Despesas Pagas':
            return 3
        elif texto == 'Inscrição de Restos a Pagar Não Processados' or 'Inscrição de RP Não Processados':
            return 4
        elif texto == 'Inscrição de Restos a Pagar Processados' or 'Inscrição de RP Processados':
            return 5
        else:
            print(texto)

    def get_funcao_despesa(self, texto):
        if self.isnumber(texto):
            return int(texto[0:2])
        elif texto == 'Despesas (Exceto Intra-Orçamentárias)' \
                or texto == 'Despesas (Intra-Orçamentárias)' \
                or texto == 'Despesas Exceto Intraorçamentárias' \
                or texto == 'Despesas Intraorçamentárias' \
                or texto == 'Despesas (Exceto Intraorçamentárias)'\
                or texto == 'Despesas (Intraorçamentárias)'\
                or texto == 'Demais Subfunções' \
                or texto[0:2] == 'FU':
            return 29
        else:
            print(texto)

    def isnumber(self, value):
        try:
            int(value[0:1])
        except ValueError:
            return False
        return True

    def get_classificacao_receita(self, texto):
        if texto == 'Deduções - FUNDEB':
            return 1
        elif texto == 'Deduções - Transferências Constitucionais':
            return 2
        elif texto == 'Outras Deduções da Receita' or texto == 'Deduções da Receita':
            return 3
        elif texto == 'Receitas Brutas Realizadas' or texto == 'Receitas Realizadas':
            return 4
        else:
            print(texto)


    def get_funcao_receita(self, texto):
        if self.isnumber(texto):
            return int(texto[0:1])
        else:
            print(texto)