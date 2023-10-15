import banco

con = banco.getConexao()
cursor = con.cursor(prepared=True)

sqlSelect = 'SELECT id_item, nome_item FROM item'
cursor.execute(sqlSelect)

consulta = cursor.fetchall()
for resultado in consulta:
    id_item, nome_item = resultado
    print(f'ID: {id_item}, nome: {nome_item}')

itemExcluirID = int(input('digite o ID do item que deseja excluir: '))


sqlDelete = 'DELETE FROM item WHERE id_item = ?'
par = [itemExcluirID,]
cursor.execute(sqlDelete,par)
con.commit()

print(cursor.rowcount, 'registro excluido')

con.close()