# coding: utf-8
from objetos_AG import Control as c, Cromossomo, Populacao
from time import time

# Recebendo dados dos arquivos
arqFretes = c.lerArquivo("arquivos/ligamagicFrete.txt")
arqPedido = c.lerArquivo("arquivos/ligamagicPedido1.txt")
arqPreco = c.lerArquivo("arquivos/ligamagicPreco.txt")
arqQtd = c.lerArquivo("arquivos/ligamagicQtd.txt")
# frete é uma variavel que com os valores de frete por loja
frete = c.geraVetorFrete(arqFretes)
#frete = c.geraVetorFrete(arqFretesTeste)
# pedido contem um Id, nome, vetor de preço por loja e vetor de quantidade por loja
pedido = c.geraPedido(arqPedido, arqPreco, arqQtd)
arqPreco.clear()
arqQtd.clear()
#pedido = c.geraPedido(arqPedidoTeste, arqPrecoTeste, arqQtdTeste)
# geracoes serve para saber quantas gerações de populações foram rodadas

arrayFitness = ["Fitness Final"]
arrayTempoTotal = ["Tempo de Execucao"]
arrayInicioPopulacao = ["Inicio Populacao"]
arraySelecao = ["Selecao"]
arrayCruzamtento = ["Cruzamento"]
arrayMutacao = ["Mutacao"]
arrayInsercao = ["Insercao"]
for tentativas in range(10):
    geracoes = 0
    # cont conta as falhas
    cont = 0
    # tam é o tamnho da população
    tam = 1000
    # falhas são quantas falhas podem ocorrer sem que seja adquirido algum cromossomo mais barato
    falhas = 100
    # Chance de ocorrer mutação, é bom 3 = 3%
    chanceMutacao = 3
    ti = time()
    # Iniciando Top1 Global
    tiCriandoPopulacao = time()
    top1 = Cromossomo.Cromossomo()
    # Iniciando o Top1 com o valor do maior int possivel para que ao ser analisado posteriormente seja excluido
    top1.preencherCromossomo(pedido, frete)
    top1.avaliacao(frete)
    # Iniciando a população
    populacao = Populacao.Populacao(pedido, frete, tam, top1)
    top1 = populacao.getTop1()
    arrayInicioPopulacao.append(time()-tiCriandoPopulacao)
    # Esse while serve como condição de parada para o codigo, sendo assim ele continuará a ser executado até que a condição de parada seja satisfeita
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
        #t2 = time()
        print("Top1: "+str(populacao.getTop1().getFitness()) + " Geração: "+str(geracoes)+" Cont: "+str(cont) +
              " Tempo de processamento: " + str(time()-ti)+"s.")
    tf = time()-ti
    arrayTempoTotal.append(tf)
    arrayFitness.append(populacao.getTop1().getFitness())
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
    print("Tempo de processamento: " + str(tf)+"s.")


c.escrever_json("pedido1.json", c.converter("Pedido1", arrayInicioPopulacao,
                                            arraySelecao, arrayCruzamtento, arrayMutacao, arrayInsercao, arrayTempoTotal, arrayFitness))
# escrever_json(arraySelecao)
# escrever_json(arrayCruzamtento)

# print(carregar_json('meu_arquivo.json'))
