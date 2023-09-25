import csv


class Conta:

    # metodo construtor
    def __init__(self, nroConta, nome, saldo=0):
        self.nroConta = nroConta
        self.nome = nome
        self.saldo = saldo

    # alterar nome
    def setNome(self, nome):
        if nome == self.nome:
            print('o nome é o mesmo')
        else:
            self.nome = nome

    # efetuar depósito
    def setDeposito(self, deposito):
        if deposito >= 0:
            self.saldo = deposito + self.saldo
            return self.saldo
        else:
            print('o deposito precisa ser um valor positivo')

    # saque
    def setSaque(self, retirada):
        ok = True
        while ok:
            saldoInicial = self.saldo
            self.saldo = self.saldo - retirada

            if (self.saldo >= 0):
                return self.saldo
            else:
                continuar = input(
                    'deseja mesmo fazer essa retirada? irá ficar com o saldo negativo ')

                if (continuar == 'sim'):

                    ok = False
                    return self.saldo
                else:
                    retirada = float(
                        input('qual o valor que deseja retirar? '))
                    print(retirada, saldoInicial)
                    if retirada <= saldoInicial:
                        saldoFinal = saldoInicial - retirada
                        self.saldo = saldoFinal
                        ok = False
                        return self.saldo
                    else:
                        ok = True
    # transerencia

    def setTransferir(self, saldoTransferido, contaDestino):
        self.saldo -= saldoTransferido
        contaDestino.saldo += saldoTransferido
        return self.saldo

    def setReceber(self, valorTransferido):
        saldoTotal = self.setDeposito(valorTransferido)
        return saldoTotal

    # imprimir valores
    def imprimaValores(self):
        print('nro da conta:', self.nroConta, '\nnome do correntista:',
              self.nome, '\nsaldo da conta:', self.saldo)


ok = True
# criando as contas, e atribuindo código e nome (valor pré-definido)
conta1 = Conta(0, 'tiago')
conta2 = Conta(1, 'lucas')
conta3 = Conta(2, 'aline')

contas = [conta1, conta2, conta3]

while ok:

    nroConta = int(input('qual é o número de sua conta? '))
    if nroConta == 0 or nroConta == 1 or nroConta == 2:
        ok = True
    else:
        input('conta não encontrada, tente novamente')
        ok = False
    # criando algo como switch
    pergunta = input(
        'qual operação deseja realizar?\n 1. alterar nome\n 2. depositar\n 3. sacar \n 4. transferir\n 5. sair\n : ')
    if pergunta == '1':
        contas[nroConta].setNome(input('insira o nome: '))
    elif pergunta == '2':
        contas[nroConta].setDeposito(float(input('valor de depositos: ')))
    elif pergunta == '3':
        contas[nroConta].setSaque(float(input('valor do saque: ')))
    elif pergunta == '4':
        outraConta = int(
            input('para qual conta deseja fazer a transferência? '))
        if nroConta == 0 or nroConta == 1 or nroConta == 2:
            contas[nroConta].setTransferir(
                float(input('valor transferido: ')), contas[outraConta])
        else:
            input('conta não encontrada, tente novamente')
    elif pergunta == '5':
        ok = False

conta1.imprimaValores()
conta2.imprimaValores()
conta3.imprimaValores()

# colocando valores em uma lista
lista = [
    ["numero da conta", "nome", "saldo"],
    [contas[0].nroConta, contas[0].nome, contas[0].saldo],
    [contas[1].nroConta, contas[1].nome, contas[1].saldo],
    [contas[2].nroConta, contas[2].nome, contas[2].saldo]
]

# abrindo arquivo
arquivo = open(
    'faculdade/programacao_para_ciencia_de_dados_unijui/exercícios/novo.csv', 'w')
# salvando arquivo em uma variável
w = csv.writer(arquivo)
# escrever a lista por linha
for i in lista:
    w.writerow(i)
# fechar arquivo
arquivo.close()
