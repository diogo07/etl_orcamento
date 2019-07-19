# import mysql.connector
import psycopg2

class Conexao:


    def conn_postgre(self, host, user, password, database):
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        return conn

    # def conn_mysql(self, host, user, password, database):
    #     conn = mysql.connector.connect(
    #         host=host,
    #         user=user,
    #         passwd=password,
    #         database=database
    #     )
    #
    #     return conn