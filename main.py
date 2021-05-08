from objetos_AG import control, Cromossomo, Populacao
from time import time
import random
import copy
import sys

# Recebendo dados dos arquivos
arqFretes = control.lerArquivo("arquivos/ligamagicFrete.txt")
arqFretesTeste = control.lerArquivo("arquivos/ligamagicFreteTeste.txt")
arqPedidoTeste = control.lerArquivo2("arquivos/pedidoteste.txt")
arqPedido1 = control.lerArquivo("arquivos/ligamagicPedido1.txt")
arqPedido2 = control.lerArquivo("arquivos/ligamagicPedido2.txt")
arqPedido3 = control.lerArquivo("arquivos/ligamagicPedido3.txt")
arqPedido4 = control.lerArquivo("arquivos/ligamagicPedido4.txt")
arqPreco = control.lerArquivo2("arquivos/ligamagicPreco.txt")
arqQtd = control.lerArquivo2("arquivos/ligamagicQtd.txt")
arqPrecoTeste = control.lerArquivo2("arquivos/ligamagicPrecoTeste.txt")
arqQtdTeste = control.lerArquivo2("arquivos/ligamagicQtdTeste.txt")
frete = control.geraVetorFrete(arqFretes)
#frete = control.geraVetorFrete(arqFretesTeste)
pedido = control.geraPedido(arqPedido1, arqPreco, arqQtd)
#pedido = control.geraPedido(arqPedidoTeste, arqPrecoTeste, arqQtdTeste)
# geracoes serve para saber quantas gerações de populações foram rodadas
geracoes = 0
# cont conta as falhas
cont = 0

# tam é o tamnho da população
tam = 20
# falhas são quantas falhas podem ocorrer sem que seja adquirido algum cromossomo mais barato
falhas = 300
tic = time()
# Iniciando Top1 Global
top1 = Cromossomo.Cromossomo()
# Iniciando o Top1 com o valor do maior int possivel para que ao ser analisado posteriormente seja excluido
top1.setFitness(sys.maxsize)
# Iniciando a população
populacao = Populacao.Populacao(pedido, frete, tam, top1)
top1 = populacao.getTop1()
'''
populacao.cruzamentoMonoPonto1(pedido, frete)
while True:
    # Esse IF serve como condição de parada para o codigo, sendo assim ele continuará a ser executado até que a condição de parada seja satisfeita
    if cont >= falhas:
        break
    populacao.insercao(pedido, frete, tam, top1)
    filho = []
    filho.append(copy.deepcopy(top1))
    filho.append(copy.deepcopy(populacao.getFilhos()[0]))
    filho.append(copy.deepcopy(populacao.getFilhos()[1]))
    for analise in filho:
        analise.mutacao(frete, 50)
        if(analise.getFitness() < top1.getFitness()):
            top1 = analise
            print("Filho:\n"+str(analise.toString()) + "Cont: "+str(cont))
            #print("asldba "+str(len(top1.getCromossomo()))+"\n")
            cont = 0
'''
populacao.cruzamentoMultiPontos(frete)
while True:
    # Esse IF serve como condição de parada para o codigo, sendo assim ele continuará a ser executado até que a condição de parada seja satisfeita
    if cont >= falhas:
        break
    populacao.insercao(pedido, frete, tam, top1)
    filho = []
    filho.append(copy.deepcopy(top1))
    filho.append(copy.deepcopy(populacao.getFilhos()[0]))
    filho.append(copy.deepcopy(populacao.getFilhos()[1]))
    for analise in filho:
        analise.mutacao(frete, 10)
        if(analise.getFitness() < top1.getFitness()):
            top1 = analise
            print("Filho:\n"+str(analise.toString()) + "Cont: "+str(cont))
            #print("asldba "+str(len(top1.getCromossomo()))+"\n")
            cont = 0

    cont += 1
    geracoes += 1
toc = time()
# print(cont)
# Top1 Global
print("Top1 Global:\n"+str(top1.toString()) + "\n")
# Top1 Populacao Atual
print("Top1 População Final:\n"+str(populacao.getTop1().toString()) + "\n")
print("Gerações: " + str(geracoes))
print("Tamanho: " + str(tam))
print("Falhas: " + str(falhas))
print("Tempo de processamento: " + str(toc-tic)+"s.")
