import pandas as pd
import csv as csv
import json

#pandas lendo o doc exel
doc_read = pd.read_excel(
    'faculdade/programacao_para_ciencia_de_dados_unijui/ei3/POP2022_Municipios_20230622.xls')
#caminho csv
doc_csv = ('faculdade/programacao_para_ciencia_de_dados_unijui/ei3/pop.csv')
#delimitar até a linha 5571
doc_read = doc_read[:5571]
#transformar xls em csv tirando o header
doc_read.to_csv(doc_csv, index=False, header=False, encoding='utf-8')
#pandas lendo o arquivo csv gerado
doc_read_csv = pd.read_csv(doc_csv)

# json_data = doc_read_csv.to_json(orient='records')
#lista dados para por no formato JSON
dados = []
#com o documento aberto leia, salva ncomo csv_file
with open(doc_csv, 'r', encoding='utf-8') as csv_file:
    #le o arquivo csv
    csvr = csv.DictReader(csv_file)
    #para cada linha no arquivo csvr
    for linha in csvr:
        uf = linha['UF']
        cod_uf = int(linha['COD. UF'])
        cod_municipio = int(linha['COD. MUNIC'])
        nome_municipio = linha['NOME DO MUNICÍPIO']
        pop = int(linha['POPULAÇÃO'])
        #verifica se já tem a entrada do estado
        verifica_existencia = next((item for item in dados if item['uf']==uf),None)
        #se sim
        if verifica_existencia:
            #adciona em municipios
            verifica_existencia['municipios'].append({
                'codigo': cod_municipio,
                'nome': nome_municipio,
                'populacao': pop
            })
        #se não
        else:
            #cria uma nova entrada
            dados.append({
                'uf': uf,
                'cod_uf': cod_uf,
                'municipios': [{
                    'codigo': cod_municipio,
                    'nome': nome_municipio,
                    'populacao': pop
                }]
            })

#salvando os dados em JSON
with open('faculdade/programacao_para_ciencia_de_dados_unijui/ei3/pop.json', 'w',encoding='utf-8') as jsonfile:
    json.dump(dados, jsonfile, indent=4)