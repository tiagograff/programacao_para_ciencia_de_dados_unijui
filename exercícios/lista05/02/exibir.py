import banco

con = banco.getConexao()
cursor = con.cursor(prepared=True)

sql = 'SELECT vendedor.id_vendedor, vendedor.nome_vendedor, venda.dt_Venda FROM vendedor INNER JOIN venda ON vendedor.id_vendedor = venda.id_vendedor WHERE YEAR (venda.dt_Venda) = 2014 AND MONTH(venda.dt_Venda) = 1;'
cursor.execute(sql)

consulta = cursor.fetchall()
for resultado in consulta:
    id_vendedor, nome_vendedor, dt_Venda = resultado
    print(f'nome: {nome_vendedor}, data da venda: {dt_Venda}')

con.commit()
con.close()