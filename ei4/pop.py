import banco
import pandas as pandas
# doc em csv
doc_csv_path = (
    'faculdade/programacao_para_ciencia_de_dados_unijui/ei4/pop.csv')
# pandas lendo o doc exel
doc_read_exel = pandas.read_excel(
    'faculdade/programacao_para_ciencia_de_dados_unijui/ei4/POP2022_Municipios_20230622.xls')
# tirar as últimas linhas
doc_read_exel = doc_read_exel[:5571]
# transformar para csv
doc_read_exel.to_csv(doc_csv_path, index=False, header=False, encoding='utf-8')
# pandas lendo o csv criado
doc_read_csv = pandas.read_csv(doc_csv_path)
#tirando espaço em branco
doc_read_csv.columns = doc_read_csv.columns.str.replace(' ', '_')
# tirando os parenteses de população
doc_read_csv['POPULAÇÃO'] = doc_read_csv['POPULAÇÃO'].str.replace(r'\(|\)', '', regex=True)
# tirando os pontos
doc_read_csv['POPULAÇÃO'] = doc_read_csv['POPULAÇÃO'].str.replace('.', '', regex=False)
doc_read_csv.to_csv(doc_csv_path, index=False)

## para o banco ##

#definindo os tipos
data_types = {
    'UF': str,
    'COD._UF': int,
    'COD._MUNIC': int,
    'NOME_DO_MUNICÍPIO': str,
    'POPULAÇÃO': int
}
# novo arquivo para o banco
doc_read_csv_data = pandas.read_csv(doc_csv_path,dtype = data_types)

## banco ##

#conexão com o banco
con = banco.getConexao()
#cursor
cursor = con.cursor(prepared=True)
# comando sql
sql = 'INSERT INTO populacao (UF, COD_UF, COD_MUNICIPIO, NOME_MUNICIPIO, POPULACAO) VALUES (?,?,?,?,?)'
# inserir valores
for index, row in doc_read_csv_data.iterrows():
    values = (row['UF'], row['COD._UF'], row['COD._MUNIC'], row['NOME_DO_MUNICÍPIO'], row['POPULAÇÃO'])
    cursor.execute(sql, values)
#commitar
con.commit()
#confirmação
print(cursor.rowcount)
#fechar conexão
con.close()
