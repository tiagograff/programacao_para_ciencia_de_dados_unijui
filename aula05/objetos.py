class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# metodos
    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade


# criar um objeto
p = Pessoa('joao', 30)

# chama metodos
print(p.getNome())
print(p.getIdade())

# herença


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula


a = Aluno('joao', 30, 9999)

print(a.getMatricula())
print(a.getIdade())
print(a.getNome())

# polimofirsmo


class Animal:
    def __init__(self):
        pass

    def locomove(self):
        pass


class Peixe(Animal):
    def locomove(self):
        print('o peixe nada')


class Elefante(Animal):
    def locomove(self):
        print('o elefante anda')


class Passaro(Animal):
    def locomove(self):
        print('o passaro voa')


peixe = Peixe()
passaro = Passaro()
elefante = Elefante()

for a in (peixe, passaro, elefante):
    a.locomove()

# medoto __str__


class Pessoaa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return 'nome: ' + self.nome + '\nidade: ' + str(self.idade)


pe = Pessoaa('joao', 30)
print(pe.__str__())
# iteradores


class Reverso:
    def __init__(self, texto):
        self.texto = texto
        self.indice = len(texto)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice == 0:
            raise StopIteration
        self.indice = self.indice - 1
        return self.texto[self.indice]


rev = Reverso('reverso')
for c in rev:
    print(c)

# tratamento de erros

while True:
    try:
        x = int(input('digite um número: '))
        break
    except ValueError:
        print('esse não é um valor válido')
    print('numero ok')

try:
    while True:
        try:
            x = int(input('digite um número: '))
            break
        except ValueError:
            print('esse não é um valor válido')
finally:
    print('numero ok')
