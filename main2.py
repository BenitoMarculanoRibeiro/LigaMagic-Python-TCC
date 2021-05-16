# coding: utf-8
from objetos_AG import c as c, Cromossomo, Populacao
from time import time
# Recebendo dados dos arquivos
arqFretes = c.lerArquivo("arquivos/ligamagicFrete.txt")
arqFretesTeste = c.lerArquivo("arquivos/ligamagicFreteTeste.txt")
arqPedidoTeste = c.lerArquivo("arquivos/pedidoteste.txt")
arqPedido1 = c.lerArquivo("arquivos/ligamagicPedido1.txt")
arqPedido2 = c.lerArquivo("arquivos/ligamagicPedido2.txt")
arqPedido3 = c.lerArquivo("arquivos/ligamagicPedido3.txt")
arqPedido4 = c.lerArquivo("arquivos/ligamagicPedido4.txt")
arqPreco = c.lerArquivo("arquivos/ligamagicPreco.txt")
arqQtd = c.lerArquivo("arquivos/ligamagicQtd.txt")
arqPrecoTeste = c.lerArquivo("arquivos/ligamagicPrecoTeste.txt")
arqQtdTeste = c.lerArquivo("arquivos/ligamagicQtdTeste.txt")
# frete é uma variavel que com os valores de frete por loja
frete = c.geraVetorFrete(arqFretes)
#frete = c.geraVetorFrete(arqFretesTeste)
# pedido contem um Id, nome, vetor de preço por loja e vetor de quantidade por loja
pedido = c.geraPedido(arqPedido2, arqPreco, arqQtd)
arqPreco.clear()
arqQtd.clear()
#pedido = c.geraPedido(arqPedidoTeste, arqPrecoTeste, arqQtdTeste)
# geracoes serve para saber quantas gerações de populações foram rodadas
geracoes = 0
# cont conta as falhas
cont = 0
# tam é o tamnho da população
tam = 1000
# falhas são quantas falhas podem ocorrer sem que seja adquirido algum cromossomo mais barato
falhas = 100
# tempo é por quanto tempo quer rodar o programa em segundos
tempo = 360
# Chance de ocorrer mutação, é bom 3 = 3%
chanceMutacao = 3

tic = time()
# Iniciando Top1 Global
top1 = Cromossomo.Cromossomo()
# Iniciando o Top1 com o valor do maior int possivel para que ao ser analisado posteriormente seja excluido
top1.preencherCromossomo(pedido, frete)
top1.avaliacao(frete)
# Iniciando a população
populacao = Populacao.Populacao(pedido, frete, tam, top1)
top1 = populacao.getTop1()
# Esse while serve como condição de parada para o codigo, sendo assim ele continuará a ser executado até que a condição de parada seja satisfeita
while cont <= falhas:
    t1 = time()
    populacao.selecao(tam)
    populacao.cruzamento(tam, pedido, frete)
    populacao.mutacao(frete, chanceMutacao)
    populacao.insercao(pedido, frete, tam)
    if(top1.getFitness() > populacao.getTop1().getFitness()):
        cont = 0
        top1 = populacao.getTop1()
    cont += 1
    geracoes += 1
    #t2 = time()
    toc = time()
    print("Top1: "+str(populacao.getTop1().getFitness()) + " Geração: "+str(geracoes)+" Cont: "+str(cont) +
          " Tempo de processamento: " + str(toc-tic)+"s.")
toc = time()
# Top1 Global
print("Top1 Global:\n"+str(top1.toString()) + "\n")
# Top1 Populacao Atual
print("Top1 População Final:\n"+str(populacao.getTop1().toString()) + "\n")
# Total de gerações
print("Gerações: " + str(geracoes))
# Tamanho da população
print("Tamanho: " + str(tam))
# Criterio de parada, quantidade de gerações sem ter melhora
print("Falhas: " + str(falhas))
# Tempo de porcessamento do AG, começa a contar do fim das
print("Tempo de processamento: " + str(toc-tic)+"s.")
