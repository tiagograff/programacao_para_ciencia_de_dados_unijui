vet = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
print(vet)
print(len(vet))
print(sorted(vet))
print(sorted(vet, reverse=True))
print(vet[0:4])
print(vet[8:])
print(vet[1:9])
print(vet[::3])

for i in vet:
    if vet[i] == 22:
        print('elemento 5 existe')
    else:
        print('elemento não existe')