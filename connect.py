import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    print("Starting connection")

    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        db='bdpython',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()
