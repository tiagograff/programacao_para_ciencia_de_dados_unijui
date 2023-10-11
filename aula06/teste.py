import mysql.connector  # driver conector


def getConexao():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='tiago123',
        database='estoque'
    )
    return con  # retorna uma conexão com o banco de dados


print(getConexao)
