from objetos_AG import control, Cromossomo, Populacao
from time import time
import random
import copy
import sys

# Recebendo dados dos arquivos
arqFretes = control.lerArquivo("arquivos/ligamagicFrete.txt")
arqFretesTeste = control.lerArquivo("arquivos/ligamagicFreteTeste.txt")
arqPedidoTeste = control.lerArquivo("arquivos/pedidoteste.txt")
arqPedido1 = control.lerArquivo("arquivos/ligamagicPedido1.txt")
arqPedido2 = control.lerArquivo("arquivos/ligamagicPedido2.txt")
arqPedido3 = control.lerArquivo("arquivos/ligamagicPedido3.txt")
arqPedido4 = control.lerArquivo("arquivos/ligamagicPedido4.txt")
arqPreco = control.lerArquivo("arquivos/ligamagicPreco.txt")
arqQtd = control.lerArquivo("arquivos/ligamagicQtd.txt")
arqPrecoTeste = control.lerArquivo("arquivos/ligamagicPrecoTeste.txt")
arqQtdTeste = control.lerArquivo("arquivos/ligamagicQtdTeste.txt")
# frete é uma variavel que com os valores de frete por loja
frete = control.geraVetorFrete(arqFretes)
#frete = control.geraVetorFrete(arqFretesTeste)
# pedido contem um Id, nome, vetor de preço por loja e vetor de quantidade por loja
pedido = control.geraPedido(arqPedido4, arqPreco, arqQtd)
arqPreco.clear()
arqQtd.clear()
#pedido = control.geraPedido(arqPedidoTeste, arqPrecoTeste, arqQtdTeste)
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
# Chance de ocorrer mutação, é bom 1 = 1%
chanceMutacao = 1
aux = []
for i in range(len(pedido[0].getCarta().getPrecos())):
    aux.append(i)

tic = time()
# Iniciando Top1 Global
top1 = Cromossomo.Cromossomo()
# Iniciando o Top1 com o valor do maior int possivel para que ao ser analisado posteriormente seja excluido
top1.preencherCromossomo(pedido, frete, aux)
top1.avaliacao(frete)
# Iniciando a população
populacao = Populacao.Populacao(pedido, frete, tam, top1, aux)
top1 = populacao.getTop1()
populacao.cruzamentoMultiPontos(frete)
# Esse while serve como condição de parada para o codigo, sendo assim ele continuará a ser executado até que a condição de parada seja satisfeita
while (time()-tic) < tempo:
    t1 = time()
    populacao.insercao2(pedido, frete, tam, top1, aux)
    if(top1.getFitness() > populacao.getTop1().getFitness()):
        cont = 0
        top1 = populacao.getTop1()
    for analise in populacao.getPais():
        if(random.randint(0, 100) < chanceMutacao):
            filho = copy.deepcopy(analise)
            filho.mutacao(frete)
            if(filho.getFitness() < top1.getFitness()):
                top1 = filho
                print("Filho: "+str(filho.toString()) +
                      "Cont: "+str(cont))
                cont = 0
            '''
            if(populacao.getTop1().getFitness() < top1.getFitness()):
                top1 = populacao.getTop1()
                print("Filho:\n"+str(filho.toString()) +
                      "Cont: "+str(cont)+"\n")
                cont = 0
            '''
    cont += 1
    geracoes += 1
    t2 = time()
    print("Geração: "+str(geracoes)+" Cont: "+str(cont) +
          " Tempo de processamento: " + str(t2-t1)+"s.")
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
