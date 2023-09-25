# comparar gabarito
def comparaGabarito(gabarito, resposta):
    numDeAcertos = 0
    # sequencia numerica
    for i in range(len(resposta)):
        if gabarito[i] == resposta[i]:
            numDeAcertos += 1
    return numDeAcertos


numQuestoes = int(input('quantas questões vai ter? '))
listaGabarito = []
listaRespotas = []
ok = True

# ate ser diferente
while numQuestoes != len(listaGabarito):
    gabarito = input('entre com um gabarito: ')
    # transforma em lista
    listaGabarito = list(gabarito)
    # "corta a lista"
    listaGabarito = listaGabarito[::2]
    # verifica tamnho de dois em dois (1 espaço)
    if numQuestoes != len(listaGabarito):
        print('o numero de questões {} difere de {}'.format(
            numQuestoes, len(listaGabarito)))
# ate ser falso
while ok:
    nome = (input('nome do aluno: '))
    resposta = input('digite as respostas de {}: '.format(nome))
    # transforma em lista
    listaRespotas = list(resposta)
    # verifica tamnho de dois em dois (1 espaço)
    listaRespotas = listaRespotas[::2]
    print('o aluno {} acertou {} questão(ões)'.format(
        nome, comparaGabarito(listaGabarito, listaRespotas)))
    continuar = input('deseja continuar? ')
    # se deseja continuar
    if ('não' == continuar):
        # acaba o laço
        ok = False
    elif ('sim' == continuar):
        ok = True
    else:
        print('valor inválido')
