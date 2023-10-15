numeros = []
i = 0
j = 0

while i < 5:
    numero = int(input('digite um numero: '))
    numeros.append(numero)
    i+=1

maior = numeros[0]
menor = numeros[0]

for j in numeros:
    if j > maior: 
        maior = j
    if j < menor: 
        menor = j
    j+=1

print('o maior valor é: {}. o menor é: {}'.format(maior,menor))
