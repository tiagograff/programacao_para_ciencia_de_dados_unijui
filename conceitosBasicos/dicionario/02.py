def media(notas):
    soma = 0
    for i in notas:
        soma += i
    resultado =  (soma / len(notas))
    return round(resultado, 2)

notas = []
alunos = {
    1: {
        'nome': 'tiago',
        'nota': 9.5
    },
    2: {
        'nome':'maria',
        'nota': 8.5
    },
    3: {
        'nome': 'joao',
        'nota': 6.5
    }
}

for i in alunos:
    notas.append(alunos[i]['nota'])

mediaDosAlunos = media(notas)
print('a média dos alunos é de: {}'.format(mediaDosAlunos))