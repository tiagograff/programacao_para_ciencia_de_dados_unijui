
import banco

con = banco.getConexao()
cursor = con.cursor()

sql = "delete from cliente where nome_cliente = 'Dionatan T'"
cursor.execute(sql)
con.commit()

print(cursor.rowcount, "registro(s) afetados(s)")

con.close
