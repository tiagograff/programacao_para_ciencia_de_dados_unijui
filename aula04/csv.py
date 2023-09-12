import csv

arq = open('faculdade/programacao_para_ciencia_de_dados_unijui/aula04/teste.csv')
dados = csv.reader(arq)
print(dados)
print(type(dados))
print()
for item in dados:
    print(item)
    print(type(item))
