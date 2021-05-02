from objetos_AG import control, Cromossomo, Populacao

arqFretes = control.lerArquivo("arquivos/ligamagicFrete.txt")
arqPedido1 = control.lerArquivo("arquivos/ligamagicPedido1.txt")
arqPedido2 = control.lerArquivo("arquivos/ligamagicPedido2.txt")
arqPedido3 = control.lerArquivo("arquivos/ligamagicPedido3.txt")
arqPedido4 = control.lerArquivo("arquivos/ligamagicPedido4.txt")
arqPreco = control.lerArquivo2("arquivos/ligamagicPreco.txt")
arqQtd = control.lerArquivo2("arquivos/ligamagicQtd.txt")

fretes = control.geraVetorFrete(arqFretes)

pedido = control.geraPedido(arqPedido1, arqPreco, arqQtd)
top1 = Cromossomo.Cromossomo()
for i in range(10):
    populacao = Populacao.Populacao(pedido, fretes, 100, top1)
    # print(populacao.toStringValor())
    top1 = populacao.getTop1()
    print("Top1 "+str(populacao.getTop1().getFitness()))
'''    print(populacao.getPais()[0].getFitness())
    print(populacao.getPais()[1].getFitness())



pedido = Pedido()
pedido.geraPedido(pedido1, vetPreco, vetQtd)

frete = Fretes()
frete.geraVetorFrete(vetFretes)

populacao = Populacao(pedido, frete, 100)
print(populacao.toStringValor())
print(populacao.getTop1().getFitness())
'''
