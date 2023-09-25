#converte para inteiro
numero = int(input('digite um número inteiro positivo: '))
if numero >= 0: 
    ##potencia (elevado)
    raiz = int(((numero)**0.5))
    #concatenação de textos com variáveis
    print('a raíz quadrada de {} arredondado é de = {}'.format(numero,raiz))
else:
    print('este número é inválido')