#limpar documentos
def clean(caminho):
    arquivo = open(caminho, 'w')
    arquivo.write('')
    arquivo.close()
    return arquivo
# transformando o arquivo em lista
def transformaEmLista(arquivo, lista):
    with arquivo:
        conteudo = arquivo.read()
        lista = conteudo.split('-')
    return lista
#transforma lista em string
def transformaEmString(lista):
    lista = '-'.join(map(str, lista))
    return lista

#inserindo valores em um documento
def insiraValoresEmUmDocumento(caminho):
    arquivoWrite = open(caminho, 'w')
    arquivoWrite.write(input('insira aqui os valores: '))
    arquivoWrite.close()
    return arquivoWrite

#arquivo no formato final
def arquivoFinal(caminho,lista,nome,acertos):
    with open(caminho, 'a') as arquivoWriteFinal:
        lista = transformaEmString(lista)
        arquivoWriteFinal.write('{};{};{};\n'.format(nome,lista,acertos))
        arquivoWriteFinal.close()
        return arquivoWriteFinal

#comparando gabarito com respostas
def comparaGabarito(gabarito, resposta):
    numDeAcertos = 0
    for i in range(len(resposta)):
        if gabarito[i] == resposta[i]:
            numDeAcertos += 1
    return numDeAcertos

#pergunta de quantas questões terão
listaGabarito = []
listaRespostas = []
listaGabarito = []
listaRespotas = []
ok = True

#limpar arquivos
clean('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exercicios/gabarito.txt')
clean('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exercicios/respostas.txt')
clean('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exercicios/listafinal.txt')

numQuestoes = int(input('quantas questões vai ter? '))

#enquanto o número de questões for diferente do tamanho do gabarito
while numQuestoes != len(listaGabarito):

    gabarito = insiraValoresEmUmDocumento('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exercicios/gabarito.txt')
    listaGabarito = transformaEmLista(open('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exercicios/gabarito.txt','r'),gabarito)

    if numQuestoes != len(listaGabarito):
        print('o numero de questões {} difere de {}'.format(
            numQuestoes, len(listaGabarito)))

# enquanto ok (não tiver mais alunos)
while ok:
    #nome
    nome = (input('nome do aluno: '))
    #resposta
    resposta = insiraValoresEmUmDocumento('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exercicios/respostas.txt')
    #transformando resposta em lista
    listaRespostas = transformaEmLista(open('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exercicios/respostas.txt','r'),resposta)
    #numero de acertos
    numDeAcertos = comparaGabarito(listaGabarito, listaRespostas)
    #arquivo final formatado
    arquivoFinal('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exercicios/listafinal.txt',listaRespostas,nome,numDeAcertos)
    #continuar looping sim ou não
    continuar = input('deseja continuar? ')
    if ('não' == continuar):
        ok = False;
    elif('sim' == continuar):
        ok = True;
    else:
        print('valor inválido')

arq = open('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exercicios/listafinal.txt', 'r')
print(arq.read())