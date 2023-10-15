num1 = int(input('entre com o primeiro valor: '))
num2 = int(input('entre com o segundo valor: '))
simbolo = input('escolhe a seguinte operação: \n' +
                '1. + \n' +
                '2. - \n' +
                '3. * \n' +
                '4. / \n')

if simbolo == '1':
    resultado = num1 + num2
    print(resultado)
elif simbolo == '2':
    resultado = num1 - num2
    print(resultado)
elif simbolo == '3':
    resultado = num1 * num2
    print(resultado)
elif simbolo == '4':
    if num2 > 0:
        resultado = num1 / num2
        print(resultado)
    else:
        print('não é possivel dividir por zero')
else:
    print('operação não encontrada')
