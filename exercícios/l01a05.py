produto = []
produtos = []
venda = []
vendas = []
numDeProduros = 0
numDeProdurosCarrinho = 0
totalVenda = 0
ok = True
ok2 = True

while ok:
    pergunta = input ('deseja adcionar um produto? ')
    if pergunta == 'sim':
        #pegando valores
        codigoProduto = int(input('digite o codigo do produto: '))
        nomeProduto = input('digite o nome do produto: ')
        valorProduto = float(input('digite o valor do produto: '))
        #adcionando em um vetor
        produto = [codigoProduto, nomeProduto, valorProduto]
        #criando uma vetor de produtos
        produtos.append(produto)
        #+1 produto a cada vez que adciona
        numDeProduros += 1
    else:
        ok = False
for i in produtos:
    print('produtos por código: {}'.format(i[0]))

while ok2:
    pergunta2 = input('deseja adcionar um item no carrinho?: ')
    if pergunta2 == 'sim':
        carrinho = int(input('adcione o código do produto para adciona-lo no carrinho: '))
        #"produto x em produtos"
        for i in produtos:
            if carrinho == i[0]:
                #adciona elementos em venda
                venda = [i[0], i[1], i[2]]
                vendas.append(venda)
                #operação de soma total de vendas
                totalVenda += i[2]
                #+1 ao carrinho
                numDeProdurosCarrinho += 1
    else:
        ok2 = False

for i in vendas:
    print('código: {}\nnome: {}\npreço: {}'.format(i[0], i[1],i[2]))

print('número total de vendas: {}'.format(numDeProdurosCarrinho))
print('total de venda: {}'.format(totalVenda))