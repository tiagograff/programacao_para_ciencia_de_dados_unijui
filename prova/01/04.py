def media(lista):
    total = 0
    for i in lista:
        total += i
        i += 1
    return total/len(lista)

ok = True
lista = []
while ok:
    numero = int(input('adcione um numero: '))
    lista.append(numero)
    pergunta = input('deseja continuar: ')
    if pergunta == 'sim':
        ok = True
    else:
        ok = False

print(media(lista))