# funcão de união
def uniao(lista1, lista2):
    auxiliar = lista1 + lista2
    return auxiliar

# função de intersecção
def interseccao(lista1, lista2):
    # set -> cria um conjunto de elementos únicos
    auxiliar1 = set(lista1)
    auxiliar2 = set(lista2)
    # interseccao de elementos (o que tem em comum)
    auxiliar3 = auxiliar1 & auxiliar2
    return set(auxiliar3)


def diferenca(lista1, lista2):
    return set(lista1) - set(lista2)


lista1 = [5, 8, 3, 2, 3, 1, 5, 4]
lista2 = [2, 7, 3, 0, 8, 1, 3, 6]

#printa o resultado
print(uniao(lista1, lista2))
print(interseccao(lista1, lista2))
#tem na lista 1 e não na 2
print(diferenca(lista1, lista2))
#tem na lista 2 e não na 1
print(diferenca(lista2, lista1))