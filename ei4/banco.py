import mysql.connector  

def getConexao():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='tiago123',
        database='populacao_data'
    )
    return con 