import json
#abre o arquivo json e atribui a arquivo
with open('faculdade/programacao_para_ciencia_de_dados_unijui/exercícios/gabarito.json', encoding='utf-8') as arquivo:
    #carrega os dados do json arquivo
    dados = json.load(arquivo)
#acessa do json x e atribui a uma variavel
gabarito = dados['gabarito']
alunos = dados['alunos']

for aluno in alunos:
    i = 0
    numDeAcertos = 0
    while i < len(aluno['respostas']):
        #compara a resposta do aluno com a do gabarito
        if aluno['respostas'][i]['resposta'] == gabarito[i]['resposta']:
            numDeAcertos += 1
        i += 1
    aluno['acertos'] = numDeAcertos

with open('faculdade/programacao_para_ciencia_de_dados_unijui/exercícios/respostas.json', 'w') as arquivoRespostas:
    #converte objetos de python para json
    json.dump(dados, arquivoRespostas, indent=4)

print('arquivo salvo com sucesso!')
