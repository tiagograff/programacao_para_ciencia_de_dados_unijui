import json

arq = open('faculdade/programacao_para_ciencia_de_dados_unijui/aula04/teste.json', 'r', encoding = 'utf-8')
dados = json.load(arq)
print(dados)
print(type(dados))
print()
for item in dados:
    print(item)
    print(type(item))


dados2 = [
    {
        "nome": "ana",
        "idade": 30
    },
    {
        "nome": "maria",
        "idade": 30
    }
]

with open('novo.json', 'w') as arquivo:
    json.dump(dados2, arquivo)

arquivo.close()
