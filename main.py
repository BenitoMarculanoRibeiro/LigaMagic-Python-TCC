from objetos_AG import control, Cromossomo, Populacao
import random
import copy
import sys

# Recebendo dados dos arquivos
arqFretes = control.lerArquivo("arquivos/ligamagicFrete.txt")
arqPedido1 = control.lerArquivo("arquivos/ligamagicPedido1.txt")
arqPedido2 = control.lerArquivo("arquivos/ligamagicPedido2.txt")
arqPedido3 = control.lerArquivo("arquivos/ligamagicPedido3.txt")
arqPedido4 = control.lerArquivo("arquivos/ligamagicPedido4.txt")
arqPreco = control.lerArquivo2("arquivos/ligamagicPreco.txt")
arqQtd = control.lerArquivo2("arquivos/ligamagicQtd.txt")
frete = control.geraVetorFrete(arqFretes)
pedido = control.geraPedido(arqPedido1, arqPreco, arqQtd)

# geracoes serve para saber quantas gerações de populações foram rodadas
geracoes = 0
# cont conta as falhas
cont = 0
# Iniciando Top1 Global
top1 = Cromossomo.Cromossomo()
# Iniciando o Top1 com o valor do maior int possivel para que ao ser analisado posteriormente seja excluido
top1.setFitness(sys.maxsize)
# tam é o tamnho da população
tam = 100
# falhas são quantas falhas podem ocorrer sem que seja adquirido algum cromossomo mais barato
falhas = 100
# Iniciando a população
populacao = Populacao.Populacao(pedido, frete, tam, top1)
while True:
    # Esse IF serve como condição de parada para o codigo, sendo assim ele continuará a ser executado até que a condição de parada seja satisfeita
    if cont >= falhas:
        break
    
    populacao = Populacao.Populacao(pedido, frete, tam, top1)
    top1 = populacao.getTop1()
    populacao.cruzamentoMultiPontos(frete)
    populacao.insercao(pedido, frete, tam, top1)
    filho = []
    filho.append(copy.deepcopy(top1))
    filho.append(copy.deepcopy(populacao.getFilhos()[0]))
    filho.append(copy.deepcopy(populacao.getFilhos()[1]))
    for analise in filho:
        analise.mutacao(frete, 50)
        if(analise.getFitness() < top1.getFitness()):
            top1 = analise
            print("Filho:\n"+str(analise.toString()) + "\nCont: "+str(cont))
            cont = 0
    cont += 1
    geracoes += 1
    print(cont)
    # Top1 Global
print("Top1 Global"+str(top1.toString()) + "\n")
# Top1 Populacao Atual
print("Top1 População Final: \n"+str(populacao.getTop1().toString()) + "\n")
print("Gerações: " + str(geracoes))
