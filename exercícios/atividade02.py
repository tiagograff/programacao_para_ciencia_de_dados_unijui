lista = [7, 4, 9, 0, 3, 2, 5, 1, 8, 6]
# printa a lista
print(lista)
# printa o tamanho da lista
print(len(lista))
# printa lista ordenada crescente
print(sorted(lista))
# printa lista ordenada descresente
print(sorted(lista, reverse=True))
# printa os primeiros 4 elementos
print(lista[0:4])
# printa últimos dois elementos da lista
print(lista[-2:])
# todos os elementos menos o primeiro e último
print(lista[1:9])
# o primeiro a cada 2 elementos
print(lista[::3])
# se existe o numero 5
if 5 in lista:
    print('esta na lista')
else:
    print('não esta na lista')