a = int(input('digite um valor inteiro para a: '))
b = int(input('digite um valor inteiro para b: '))

if b == 0:
    print('não é possivel calcular a divisão')
else:
    resultado = a/b
    print('o resultado é: {}'.format(resultado))

c = int(input('digite um valor inteiro para c: '))
d = int(input('digite um valor inteiro para d: '))

if c > d:
    print('{} é maior que {}'.formatc(c, d))
elif c == d:
    print('{} é igual à {}'.format(c, d))
else:
    print('{} é menor que {}'.format(c, d))

e = 1
while e <=10:
    print(e)
    e += 1
    if e == 5:
        break
    if e == 8:
        continue

f = [1,2,3,4,5]
for x in f:
    print(x)

for x in range(6):
    print(x)