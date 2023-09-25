#limpar documentos
def clean(caminho):
    arquivo = open(caminho, 'w')
    arquivo.write('')
    arquivo.close()
    return arquivo
#inserir valores em um produto
def inserirProduto(caminho,lista):
    arquivo = open(caminho, 'a')
    arquivo.write(('codigo: {}, nome: {}, valor: {}'.format(lista[0], lista[1], lista[2])))
    arquivo.close()
    return arquivo
#inserir produtos em uma lista
def inserirProdutoEmLista(caminho, lista, aux):
    arquivo = open (caminho, 'a')
    arquivo.write('produto {}: código: {}, nome: {} e valor: {}\n'.format(aux, lista[0],lista[1],lista[2]))
    arquivo.close()
    return arquivo
#adcionar o valor total a lista final
def valorTotal(caminho,total):
    arquivo = open (caminho, 'a')
    arquivo.write('valor total = {}\n'.format(total))
    arquivo.close()
    return arquivo

ok = True
ok2 = True
carrinho = []
produto = []
produtos = []
venda =[]
mostraProdutos= []
aux = 1
valores = []

#limpar arquivos
clean('faculdade/programacao_para_ciencia_de_dados_unijui/exercícios/produto.txt')
clean('faculdade/programacao_para_ciencia_de_dados_unijui/exercícios/venda.txt')

#primeiro enquanto for verdadeiro
while ok:
    #adcionar um produto
    print('adcione um produto...')
    #definir valores
    codigoProduto = input('entre com o codigo do produto: ')
    nomeProduto = input('entre com o nome produto: ')
    valorProdutoStr = input('entre com o valor produto: ')
    valorProduto = valorProdutoStr
    produto = [codigoProduto, nomeProduto, valorProduto]
    #inserir valores em um documento txt
    inserirProduto('faculdade/programacao_para_ciencia_de_dados_unijui/exercícios/produto.txt',produto)
    produtos.append(produto)
    #inserir produtos uma lista de venda
    inserirProdutoEmLista('faculdade/programacao_para_ciencia_de_dados_unijui/exercícios/venda.txt',produto,aux)
    adcionar = input('deseja adcionar outro produto a lista de produtos? ou deseja sair? ')
    if adcionar == 'sim':
        aux +=1
        produtos[::4]
    elif adcionar == 'não':
        print('ok...')
    elif adcionar == 'sair':
        ok = False

#segundo enquanto for verdadeiro
while ok2:
    #escolher o produto para botar a venda
    mostraProduto = input('qual produto você deseja adcionar a venda? ')
    for prod in produtos:
        #se o código for igual adicione a venda o valor 2 da lista (preco)
        if mostraProduto == prod[0]:
            venda.append(prod[2])
    pergunta = input('deseja adcionar mais um produto para venda? ')
    if pergunta == 'não':
        ok2 = False
    else:
        ok2 = True
#transformar a lista de venda string em int
for val in venda:
    valores.append(int(val))
somaTotal = sum(valores)

#formatar arquivo final com as informacoes finais
arquivoFinal = valorTotal('faculdade/programacao_para_ciencia_de_dados_unijui/exercícios/venda.txt',somaTotal)
arquivoFinal = open('faculdade/programacao_para_ciencia_de_dados_unijui/exercícios/venda.txt','r')
print(arquivoFinal.read())