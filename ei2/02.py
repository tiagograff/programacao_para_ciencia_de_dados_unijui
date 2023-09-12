ok  = True
dicionario = {}
posicao = 0

while ok:
    numero = int(input('digite um valor inteiro maior que zero: '))
    if numero > 0:
        if numero in dicionario:
            dicionario[numero] +=1
        else:
            dicionario[numero] = 1
    else:
        ok = False
print(dicionario)