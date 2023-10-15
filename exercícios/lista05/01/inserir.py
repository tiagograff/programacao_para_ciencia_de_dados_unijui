import banco

def defineID():
    cursor.execute('SELECT MAX(id_item) FROM item')
    ultimoID = cursor.fetchone()[0]
    if ultimoID is None:
        return 1
    else:
        return ultimoID + 1

con = banco.getConexao()
cursor = con.cursor(prepared = True)

idGrupo = int(input('selecione o id do produto \n'+
                    '4. livraria\n'+
                    '5. informatica\n'+
                    '6. eletronicos\n: '))
idItem = defineID()
nomeItem = input('qual é o nome do item? ')
unidade = input('qual é a unidade? ')
preco = float(input('quanto custa este produto: '))
preco = round(preco,2)
quantidade = int(input('quantidade em estoque do produto? '))

print(preco)

sql = 'INSERT INTO item (id_grupo, id_item, nome_item, unidade, preco, qtde_estoque) VALUES (?,?,?,?,?,?)'
par = [
    (idGrupo, idItem, nomeItem, unidade, preco, quantidade)
]

cursor.executemany(sql,par)
con.commit()
print(cursor.rowcount, 'produto inserido com suecesso!')

con.close()