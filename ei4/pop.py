import banco
import pandas as pd
import csv as csv

# # pandas lendo o doc exel
# doc_read = pd.read_excel(
#     'faculdade/programacao_para_ciencia_de_dados_unijui/ei4/POP2022_Municipios_20230622.xls')
# # caminho csv
# doc_csv = ('faculdade/programacao_para_ciencia_de_dados_unijui/ei4/pop.csv')
# # delimitar até a linha 5571
# doc_read = doc_read[:5571]
# # transformar xls em csv tirando o header
# doc_read.to_csv(doc_csv, index=False, header=False, encoding='utf-8')
# # pandas lendo o arquivo csv gerado
# doc_read_csv = pd.read_csv(doc_csv)

arq = open('faculdade/programacao_para_ciencia_de_dados_unijui/ei4/pop.csv')
dados = csv.reader(arq)
print(dados)
# print(type(dados))
# print()
for item in dados:
    print(item)
    print(type(item))


# # pegar conexao
# con = banco.getConexao()
# cursor = con.cursor(prepared=True)
# # comando sql
# sql = 'INSERT INTO populacao (UF, COD_UF, COD_MUNICIPIO, NOME_MUNICIPIO, POPULACAO) VALUES (?,?,?,?,?)'
# # inserir valores
# # par = [
# #     ('RS', 1, 1, 'Coronel Barros',3000)
# # ]

# for index, linha in doc_read_csv.iterlinhas():
#     valores = (linha['UF'], linha['COD_UF'], linha['COD_MUNICIPIO'],
#                linha['NOME_MUNICIPIO'], linha['POPULACAO'])
#     cursor.execute(sql, valores)

# con.commit()
# print(cursor.rowcount, "registros inseridos")

# con.close()
