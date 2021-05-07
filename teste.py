from objetos_AG import control, Cromossomo, Populacao, gene
import random
import copy
import sys

# Recebendo dados dos arquivos
arqFretes = control.lerArquivo("arquivos/ligamagicFreteTeste.txt")
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
pedido = control.geraPedido(arqPedidoTeste, arqPrecoTeste, arqQtdTeste)
# print(pedido[1].getCarta().getPrecos()[72])
num = 0
for i in pedido:
    num += int(i.getQtd())
#print("Qtd estimado: " + str(86**num))
print(len(pedido))
top1 = Cromossomo.Cromossomo()
top1.setFitness(sys.maxsize)
geracoes = 0
for i in range(6):
    # for k in range(86):
    copiaPedido = copy.deepcopy(pedido)
    loja1 = copiaPedido[0].getCarta().getQtd()[i]

    cromossomo = Cromossomo.Cromossomo()
    if(int(loja1) > 0):
        gene1 = gene.Gene()
        gene1.setCarta(copiaPedido[0].getCarta())
        gene1.setLoja(i)
        copiaPedido[0].getCarta().menos1(i)
        cromossomo.getCromossomo().append(gene1)
        # cromossomo.getCromossomo().append(gene3)
        cromossomo.avaliacao(frete)

        if(cromossomo.getFitness() < top1.getFitness()):
            top1 = cromossomo
            print("Filho:\n"+str(cromossomo.toString()) +
                  "Cont: "+str(geracoes)+"\n")
    geracoes += 1
    # print(geracoes)


'''
for i in range(6):
    for j in range(6):
        # for k in range(86):
        copiaPedido = copy.deepcopy(pedido)
        loja1 = copiaPedido[0].getCarta().getQtd()[i]
        loja2 = copiaPedido[1].getCarta().getQtd()[j]
        #loja3 = copiaPedido[1].getCarta().getQtd()[k]

        cromossomo = Cromossomo.Cromossomo()
        if(int(loja1) > 0):
            gene1 = gene.Gene()
            gene1.setCarta(copiaPedido[0].getCarta())
            gene1.setLoja(i)
            copiaPedido[0].getCarta().menos1(i)
            if(int(loja2) > 0):
                gene2 = gene.Gene()
                gene2.setCarta(copiaPedido[1].getCarta())
                gene2.setLoja(j)
                copiaPedido[1].getCarta().menos1(i)
                if(int(loja3) > 0):
                gene3 = gene.Gene()
                gene3.setCarta(copiaPedido[1].getCarta())
                gene3.setLoja(k)
                copiaPedido[1].getCarta().menos1(i)
                cromossomo.getCromossomo().append(gene1)
                cromossomo.getCromossomo().append(gene2)
                # cromossomo.getCromossomo().append(gene3)
                cromossomo.avaliacao(frete)

                if(cromossomo.getFitness() < top1.getFitness()):
                    top1 = cromossomo
                    print("Filho:\n"+str(cromossomo.toString()) +
                          "Cont: "+str(geracoes)+"\n")
        geracoes += 1
        # print(geracoes)
'''


print("Top1 Global:\n"+str(top1.toString()) + "\n")
print("Gerações: " + str(geracoes))
