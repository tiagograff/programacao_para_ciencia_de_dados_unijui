num1 = int(input('digite um número inteiro: '))
num2 = int(input('digite um número inteiro: '))

if num1 == num2:
    print('os números são iguais')
elif num1 > num2:
    aux = (num1 - num2)
    print('o numero {} é maior que o número {} por {} de diferença.'.format(num1, num2, aux))
else:
    aux = (num2 - num1)   
    print('o numero {} é maior que o menor {} por {} de diferença.'.format(num2, num1, aux)) 
