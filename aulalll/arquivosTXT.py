#leitura

arq = open('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exemplo1.txt', 'r', encoding='utf-8')
print(arq.read())
print('posição atual do arquivo:',arq.tell())
arq.seek(11,0)
print(arq.read(7))

#for e lista

for c in arq:
    print(c)

l = list(arq.read())
print(l)

#escrevendo

texto = 'escrevendo no arquivo'
arq = open('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exemplo1.txt', 'w', encoding='utf-8')
arq.write(texto)
arq.close
arq = open('exemplo1.txt','r')
print(arq.read())

#escrevendo por input

texto = input('digite o texto do arquivo:')
arq = open('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exemplo1.txt', 'w', encoding='utf-8')
arq.write(texto)
arq.close
arq = open('exemplo1.txt', 'r')
print(arq.read())

#escrevendo no final

texto = input('digite o texto do arquivo:')
arq = open('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exemplo1.txt', 'a', encoding='utf-8')
arq.write(texto)
arq.close
arq = open('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exemplo1.txt', 'r', encoding='utf-8')
print(arq.read())

# escrevendo através de uma lista

lista = ['linha1\n','linha2\n','linha3']
arq = open('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exemplo1.txt', 'w', encoding='utf-8')
arq.writelines(lista)
arq.close()
arq = open('faculdade/programacao_para_ciencia_de_dados_unijui/aulalll/exemplo1.txt', 'r', encoding='utf-8')
print(arq.read())