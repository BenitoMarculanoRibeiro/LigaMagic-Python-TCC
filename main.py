from objetos_AG import control, Cromossomo, Populacao
import random
import copy
import sys

arqFretes = control.lerArquivo("arquivos/ligamagicFrete.txt")
arqPedido1 = control.lerArquivo("arquivos/ligamagicPedido1.txt")
arqPedido2 = control.lerArquivo("arquivos/ligamagicPedido2.txt")
arqPedido3 = control.lerArquivo("arquivos/ligamagicPedido3.txt")
arqPedido4 = control.lerArquivo("arquivos/ligamagicPedido4.txt")
arqPreco = control.lerArquivo2("arquivos/ligamagicPreco.txt")
arqQtd = control.lerArquivo2("arquivos/ligamagicQtd.txt")
frete = control.geraVetorFrete(arqFretes)
pedido = control.geraPedido(arqPedido1, arqPreco, arqQtd)

#Top1 Global
top1 = Cromossomo.Cromossomo()
top1.setFitness(sys.maxsize)
populacao = Populacao.Populacao(pedido, frete, 100, top1)
for i in range(30):
    populacao = Populacao.Populacao(pedido, frete, 100, top1)
    top1 = populacao.getTop1()
    populacao.cruzamentoMultiPontos(frete)
    filho = []
    filho.append(copy.deepcopy(top1))
    filho.append(copy.deepcopy(populacao.getFilhos()[0]))
    filho.append(copy.deepcopy(populacao.getFilhos()[1]))
    for analise in filho:
        analise.mutacao(frete, 90)
        if(analise.getFitness() < top1.getFitness()):
            top1 = analise
            print("Filho "+str(analise.getFitness()))
    #Top1 Global
    print("Top1 "+str(top1.getFitness()))
    #Top1 Populacao Atual
    print("Top1 "+str(populacao.getTop1().getFitness()) + "\n")
