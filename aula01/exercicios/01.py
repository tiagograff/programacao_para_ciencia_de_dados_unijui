veta = [1, 4, 3, 6, 8, 3, 5, 8]
vetb = [5, 3, 7, 9, 2, 4, 6, 9]


def union(x, y):
    aux = x + y
    return aux


def intersection(x,y):
    aux1 = set(x)
    aux2 = set(y)
    aux3 = aux1 & aux2
    listaf = list(aux3)
    return listaf

def difference(x,y):
    aux = set(x) - set(y)
    return aux

print(union(veta, vetb))
print(intersection(veta,vetb))
print(difference(veta,vetb))