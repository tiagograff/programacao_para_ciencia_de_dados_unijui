ok = True
ok2 = True
carrinho = []
produto = []
produtos = []
venda =[]
mostraProdutos= []

while ok:
    print('adcione um produto...')
    codigoProduto = input('entre com o codigo do produto: ')
    nomeProduto = input('entre com o nome produto: ')
    valorProdutoStr = input('entre com o valor produto: ')
    valorProduto = int(valorProdutoStr)

    produto = [codigoProduto, nomeProduto, valorProduto]
    produtos.append(produto)
    adcionar = input('deseja adcionar outro produto a lista de produtos? ou deseja sair? ')
    if adcionar == 'sim':
        produtos[::4]
    elif adcionar == 'não':
        print('ok...')
    elif adcionar == 'sair':
        ok = False
print(produtos)
print('deseja colocar qual produto no carrinho? ')

while ok2:
    
    mostraProduto = input('qual produto você deseja adcionar a venda?')
    for prod in produtos:
        if mostraProduto == prod[0]:
            venda.append(prod[2])
    pergunta = input('deseja adcionar mais um produto para venda?')
    if pergunta == 'não':
        ok2 = False
    else:
        ok2 = True
print(sum(venda))