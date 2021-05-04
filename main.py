from objetos_AG import control, Cromossomo, Populacao
import random
import copy

arqFretes = control.lerArquivo("arquivos/ligamagicFrete.txt")
arqPedido1 = control.lerArquivo("arquivos/ligamagicPedido1.txt")
arqPedido2 = control.lerArquivo("arquivos/ligamagicPedido2.txt")
arqPedido3 = control.lerArquivo("arquivos/ligamagicPedido3.txt")
arqPedido4 = control.lerArquivo("arquivos/ligamagicPedido4.txt")
arqPreco = control.lerArquivo2("arquivos/ligamagicPreco.txt")
arqQtd = control.lerArquivo2("arquivos/ligamagicQtd.txt")

fretes = control.geraVetorFrete(arqFretes)

pedido = control.geraPedido(arqPedido1, arqPreco, arqQtd)

#print(pedido[random.randint(1, len(pedido)-2)].getCarta().getNome())


top1 = Cromossomo.Cromossomo()
top1.preencherCromossomo(pedido, fretes)
for i in range(10):
    populacao = Populacao.Populacao(pedido, fretes, 100, top1)
    top1 = populacao.getTop1()
    populacao.cruzamentoMonoPonto(pedido, fretes)
    top1.mutacao(20)
    print("Pai " + str(populacao.getPais()[0].getFitness()))
    print("Mãe " + str(populacao.getPais()[1].getFitness()))
    print("Filho " + str(populacao.getFilho().getFitness()))
    print("Top1 "+str(populacao.getTop1().getFitness()) + "\n")


'''

top1 = Cromossomo.Cromossomo()
for i in range(10):
    populacao = Populacao.Populacao(pedido, fretes, 100, top1)
    # print(populacao.toStringValor())
    top1 = populacao.getTop1()
    print("Top1 "+str(populacao.getTop1().getFitness()))
    print(populacao.getPais()[0].getFitness())
    print(populacao.getPais()[1].getFitness())


for item in pedido:
    print("Carta: "+str(item.getCarta().getNome()) +
          " Id: "+str(item.getCarta().getId()))

print("\n\n")
pai = Cromossomo.Cromossomo()
pai.preencherCromossomo(pedido, fretes)
mae = Cromossomo.Cromossomo()
mae.preencherCromossomo(pedido, fretes)
pais = [mae,pai]

for item in pais:
    print(item.toString())
ponto = pedido[random.randint(1, len(pedido)-2)].getCarta().getId()
print("Id Ponto: " + str(ponto))
pos = 0
filho = Cromossomo.Cromossomo()
status = True
for pos in range(len(pai.getCromossomo())):
    if(int(pai.getCromossomo()[pos].getCarta().getId()) == int(ponto)):
        status=False
    if(status):
        #print(pai.getCromossomo()[pos].getCarta().getNome())
        filho.getCromossomo().append(pai.getCromossomo()[pos])
    else:
        filho.getCromossomo().append(mae.getCromossomo()[pos])
    pos += 1
filho.avaliacao(fretes)

print(filho.toString())



pedido = Pedido()
pedido.geraPedido(pedido1, vetPreco, vetQtd)

frete = Fretes()
frete.geraVetorFrete(vetFretes)

populacao = Populacao(pedido, frete, 100)
print(populacao.toStringValor())
print(populacao.getTop1().getFitness())
'''
