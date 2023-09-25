numero = int(input('digite um número inteiro positivo: '))
#se o resto da divisão de número por 2 for igual a zero
if numero % 2 == 0:
    print('{} é par'.format(numero))
else:
    print('{} é ímpar'.format(numero))