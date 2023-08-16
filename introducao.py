print('ola mundo')
print(15+20)

print(type("13"))
print(type(False))

print('''texto em mais
de uma linha''')

print('texto \n' * 3 + 'concatenando')

a, b, c = 'texto', 5, 5.5
print(type(a))
print(type(b))
print(type(c))

# conversao de variavel
d = str(5)
e = float(5)
f = bool(0)  # false 1... true
print('d = ', d, '\t tipo: ', type(d))
print('d = ', e, '\t tipo: ', type(e))
print('d = ', f, '\t tipo: ', type(f))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[0])
print(lista[1])
print(type(lista))
print(len(lista))
lista[0] = 11
print(lista)

listah = [3.5, 4, '5']
print(listah)

resultado = lista[1] + listah[0]
print(resultado)
print(type(resultado))

resultado = lista + listah
print(resultado)

l1 = [1, 2] * 3
l2 = [1, 2] * 3 * 3
print(l1, l2)

# quebrar caracteres de uma string
g = 'texto'
h = list(g)
print(h)

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
print(lista2[0:3])
print(lista2[:5])
print(lista2[5:])
print(lista2[0:8:3])
print(lista2[::4])

lista3 = [1, 4]
print(4 in lista3)

lista4 = [1, 2, 3, 4]
lista5 = lista4
lista6 = lista4.copy()
lista5[0] = 888
lista6[0] = 999
print(id(lista4), '', lista4)
print(id(lista5), '', lista4)
print(id(lista6), '', lista6)

lista7 = [[1, 2, 3], [4, 5, 6]]
print(lista7)
print(lista7[0])
print(lista7[1][2])
i = [7, 8, 9, 10]
lista7.append(i)
print(lista7)

#tuplas

lista8 = (1, 2, 3)
print(type(lista8))
t1 = (1)
t2 = (1,)  # tupla

j = {1, 2, 3, 4, 5}
print(j)
print(type(j))

h = set('12345')
print(type(h))

dicionario = {422: 'elemento 422', 513: 'elemento 513',}
print(type(dicionario))