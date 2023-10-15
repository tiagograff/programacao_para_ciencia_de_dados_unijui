import banco
import json

con = banco.getConexao()
cursor = con.cursor(prepared=True)

sqlSelect = 'SELECT * FROM venda'
cursor.execute(sqlSelect)

transferir = cursor.fetchall()

con.close()

vendas=[]

for coluna in transferir:
    estoque = {
        'id_venda': coluna[0],
        'id_vendedor': coluna[1],
        'id_cliente': coluna[2],
        'dt_Venda': coluna[3].strftime('%Y-%M-%D'),
        'vl_total_venda': float(coluna[4])
    }
    vendas.append(estoque)

sqlToJson = 'SELECT * INTO OUTFILE'

with open('C:/Users/tiago/code/faculdade/programacao_para_ciencia_de_dados_unijui/exercícios/lista05/03/doc.json', 'w') as doc_json:
    json.dump(vendas, doc_json)

print('dados transferidos com sucesso!')