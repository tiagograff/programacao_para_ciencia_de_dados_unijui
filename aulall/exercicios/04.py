def comparaGabarito(gabarito, resposta):
    numDeAcertos = 0
    for i in range(len(resposta)):
        if gabarito[i] == resposta[i]:
            numDeAcertos += 1
    return numDeAcertos

numQuestoes = int(input('quantas questões vai ter? '))
listaGabarito = []
listaRespotas = []
ok = True

while numQuestoes != len(listaGabarito):
    gabarito = input('entre com um gabarito: ')

    listaGabarito = list(gabarito)
    listaGabarito = listaGabarito[::2]

    if numQuestoes != len(listaGabarito):
        print('o numero de questões {} difere de {}'.format(
            numQuestoes, len(listaGabarito)))

while ok:
    nome = (input('nome do aluno: '))
    resposta = input('digite as respostas de {}: '.format(nome))
    listaRespotas = list(resposta)
    listaRespotas = listaRespotas[::2]
    print('o aluno {} acertou {} questão(ões)'.format(
        nome, comparaGabarito(listaGabarito, listaRespotas)))
    continuar = input('deseja continuar? ')
    if ('não' == continuar):
        ok = False;
    elif('sim' == continuar):
        ok = True;
    else:
        print('valor inválido')
