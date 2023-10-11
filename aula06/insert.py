
import banco

con = banco.getConexao()
# ferramenta de manipulção de informação no banco de dados (prepared = True) -> agiliza o processo do bd,
cursor = con.cursor()

# (?,?)
sql = 'INSERT  INTO cliente (id_cliente, nome_cliente, id_tipo_cliente) VALUES (default, %s, %s)'
par = ('Dionatan', 5)  # parametros
cursor.execute(sql, par)

con.commit()

print(cursor.rowcount, 'registro inserido')  # quantas linhas foram afetadas
print('id_cliente: ', cursor.lastrowid)  # pegar o último id

con.close()  # encerrar a conexão
