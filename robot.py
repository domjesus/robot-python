import csv
# from with_sqlite import Sqlite_connect
from connect import *

from connect import conecta


def insere(siape):
    # INSERE UM REGISTRO NA BASE DE DADOS
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = 'INSERT INTO siapes (siape) VALUES ' \
                '(%s)'
            cursor.execute(sql, siape)
            conexao.commit()


def list():
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM siapes')
            resultado = cursor.fetchall()
            # print(resultado)
            # make_csv(resultado)

            # for linha in resultado:
            # print(type(linha))
            # print(f"Siape {linha['siape']} repete: {linha['qtde_siape']}")
            # print(linha)
            # make_csv(linha)
            # print(f"Id: {linha['id']} Siape: {linha['siape']}")
            # print(linha['id'])
            return resultado


def ler_csv():
    print("Reading .csv file")
    dados = []
    with open("Siapes.csv") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            dados.append(row[1])

    return dados


def make_csv(row={}):
    print("Writing in .csv file")
    with open('Siapes.csv', 'w', newline='') as f:
        header = ['id', 'siape', 'status']
        # mydata = [
        #     {'nome': 'jose', 'idade': 25},
        #     {'nome': 'maria', 'idade': 26},
        #     {'nome': 'antonio', 'idade': 55},
        #     {'nome': 'manoel', 'idade': 35},
        #     {'nome': 'filomena', 'idade': 45},
        #     {'nome': 'manoel', 'idade': 35},
        #     {'nome': 'josefa', 'idade': 65},
        #     {'nome': 'paulo', 'idade': 47},
        #     {'nome': 'nilo', 'idade': 65},
        # ]
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(row)
        # f.close()


# def sqlitequery():

    # Insert a row of data

# ler_csv()
list()
# sqlitequery()
# query_sqlite = Sqlite_connect()
# query_sqlite.create_table()
# query_sqlite.insert(['2006-01-05', 'BUY', 'RHAT', 100, 60.14])
# query_sqlite.list()
# make_csv()
