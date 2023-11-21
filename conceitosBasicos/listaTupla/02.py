lista = ['abacaxi', 'barco', 'casa', 'destino', 'elefante']
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)

lista5 = []
tuplaImpar = ()

for i in lista:
    if len(i) == 5:
        lista5.append(i)

for j in lista5:
    print('palavras com 5 letras {}'.format(j))

for k in tupla:
    if k % 2 == 1:
        tuplaImpar += (k,)

for l in tuplaImpar:
    print('o número {} é impar'.format(l))
