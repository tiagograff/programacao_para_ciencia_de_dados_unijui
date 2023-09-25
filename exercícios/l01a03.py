numero1 = int(input('digite um número inteiro: '))
numero2 = int(input('digite outro número inteiro: '))

if numero1 == numero2:
    print('os números são iguais')
else:
    if numero1 > numero2:
        diferenca = numero1 - numero2
        print('o número {} é maior, com uma diferença de {}'.format(numero1,diferenca))
    else:
        diferenca = numero2 - numero1
        print('o número {} é maior, com uma diferença de {}'.format(numero2,diferenca))