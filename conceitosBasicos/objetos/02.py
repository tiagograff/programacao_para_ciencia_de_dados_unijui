class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade


newPessoa = Pessoa(nome='Tiago', idade=23)
print(newPessoa.get_nome())
print(newPessoa.get_idade())
