# coding: utf-8
from objetos_AG import Control as c, Cromossomo, Populacao
from time import time

arrayFitness = ["Fitness Final"]
arrayTempoTotal = ["Tempo de Execucao"]
arrayInicioPopulacao = ["Inicio Populacao"]
arraySelecao = ["Selecao"]
arrayCruzamtento = ["Cruzamento"]
arrayMutacao = ["Mutacao"]
arrayInsercao = ["Insercao"]
for tentativas in range(10):
    arqFretes = c.lerArquivo("arquivos/ligamagicFrete.txt")
    arqPedido = c.lerArquivo("arquivos/ligamagicPedido4.txt")
    arqPreco = c.lerArquivo("arquivos/ligamagicPreco.txt")
    arqQtd = c.lerArquivo("arquivos/ligamagicQtd.txt")
    frete = c.geraVetorFrete(arqFretes)
    pedido = c.geraPedido(arqPedido, arqPreco, arqQtd)
    arqPreco.clear()
    arqQtd.clear()
    geracoes = 0
    cont = 0
    tam = 1000
    falhas = 100
    chanceMutacao = 3
    ti = time()
    tiCriandoPopulacao = time()
    top1 = Cromossomo.Cromossomo()
    top1.preencherCromossomo(pedido, frete)
    top1.avaliacao(frete)
    populacao = Populacao.Populacao(pedido, frete, tam, top1)
    top1 = populacao.getTop1()
    arrayInicioPopulacao.append(time()-tiCriandoPopulacao)
    for entativas in range(falhas):
        tiSelecao = time()
        populacao.selecao(tam)
        arraySelecao.append(time()-tiSelecao)
        tiCruzamento = time()
        populacao.cruzamento(tam, pedido, frete)
        arrayCruzamtento.append(time()-tiCruzamento)
        tiMutacao = time()
        populacao.mutacao(frete, chanceMutacao)
        arrayMutacao.append(time()-tiMutacao)
        tiInsercao = time()
        populacao.insercao(pedido, frete, tam)
        arrayInsercao.append(time()-tiInsercao)
        if(top1.getFitness() > populacao.getTop1().getFitness()):
            cont = 0
            top1 = populacao.getTop1()
        cont += 1
        geracoes += 1
        print("Top1: "+str(populacao.getTop1().getFitness()) + " Geração: "+str(geracoes)+" Cont: "+str(cont) +
              " Tempo de processamento: " + str(time()-ti)+"s.")
    tf = time()-ti
    arrayTempoTotal.append(tf)
    arrayFitness.append(populacao.getTop1().getFitness())
    print("Top1 Global:\n"+str(top1.toString()) + "\n")
    print("Gerações: " + str(geracoes))
    print("Tamanho: " + str(tam))
    print("Falhas: " + str(falhas))
    print("Tempo de processamento: " + str(tf)+"s.")


c.escrever_json("pedido4.json", c.converter("Pedido4", arrayInicioPopulacao,
                                            arraySelecao, arrayCruzamtento, arrayMutacao, arrayInsercao, arrayTempoTotal, arrayFitness))
