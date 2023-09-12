def uniao(vet1, vet2):
    return vet1 + vet2


def intersecao(vet1, vet2):
    aux1 = set(vet1)
    aux2 = set(vet2)
    lista = aux1 & aux2
    lista = list(lista)
    return lista

def diferenca(vet1, vet2):
    lista1 = set(vet1) - set(vet2)
    lista2 = set(vet2) - set(vet1)
    return lista1, lista2

def diferencaNumero(count1,count2):
    if count1 > count2:
        return count1 - count2
    else: 
        return count2 - count1

conjunto1 = []
conjunto2 = []
count1 = 0
count2 = 0
ok = True

while ok:
    fruta = input('digite as frutas do primeiro conjunto: ')
    conjunto1.append(fruta)
    count1 += 1
    pergunta1 = input('deseja adcionar mais uma fruta ao primeiro conjunto: ')
    if pergunta1 == 'sim':
        ok
    else:
        ok = False

ok = True

while ok:
    fruta = input('digite as frutas do segundo conjunto: ')
    conjunto2.append(fruta)
    count2 += 1
    pergunta2 = input('deseja adcionar mais uma fruta ao segundo conjunto: ')
    if pergunta2 == 'sim':
        ok
    else:
        ok = False

print('a união é: ', uniao(conjunto1, conjunto2))
print('a interseção é: ', intersecao(conjunto1, conjunto2))
print('a diferença é: ', diferenca(conjunto1, conjunto2))
print('a diferença em numero de frutas é de: ', diferencaNumero(count1, count2))