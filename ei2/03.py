def calculaMedia(nota1, nota2):
    return (nota1 + nota2)/2


def verificaAprovacao(total):
    if total >= 60:
        situacao = 'aprovado'
    else:
        situacao = 'reprovado'
    return situacao


alunos = {
    'aluno': {

    }
}

countAprovados = 0
countReprovados = 0
media1 = 0
media2 = 0
mediaMedia = 0

print('\n--- bem vindo ao sistema de notas ---\n')
nroDeAlunos = int(input('quantos alunos são? '))
total = nroDeAlunos
while nroDeAlunos != 0:
    nome = input('adicione o nome do aluno: ')
    nota1 = int(input('nota 1: '))
    nota2 = int(input('nota 2: '))
    media = calculaMedia(nota1, nota2)
    situacao = verificaAprovacao(media)

    for index in alunos:
        alunos[index][nome] = [nota1, nota2, media, situacao]
        nroDeAlunos -= 1
        if alunos[index][nome][3] == 'aprovado':
            countAprovados += 1
        else:
            countReprovados += 1
        media1 = alunos[index][nome][0] + media1
        media2 = alunos[index][nome][1] + media2
        mediaMedia = alunos[index][nome][2] + mediaMedia

percentualReprovados = (countReprovados/total)*100
percentualAprovados = (countAprovados/total)*100

media1 = media1/total
media2 = media2/total
mediaMedia = mediaMedia/total

print(alunos)
print('\nnumero de aprovados:', countAprovados, '\nnúmero de reprovados:', countReprovados, '\npercentual de reprovados:', percentualReprovados,
      '\npercentual de aprovados:', percentualAprovados, '\nmedia da nota 1:', media1, '\nmedia da nota 2:', media2, '\nmedia da media:', mediaMedia)
