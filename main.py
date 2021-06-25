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

geracoes = 0
cont = 0
tam = 1000
falhas = 100
chanceMutacao = 3
ti = time()
print("Iniciando Geração: "+str(cont) +
      " | " + str(str(time()-ti).replace(".", ",")))
tiCriandoPopulacao = time()
top1 = Cromossomo.Cromossomo()
top1.preencherCromossomo(pedido, frete)
top1.avaliacao(frete)
populacao = Populacao.Populacao(pedido, frete, tam, top1)
top1 = populacao.getTop1()
print("Top1: "+str(populacao.getTop1().getFitness()) + " | Geração: "+str(geracoes) +
      " | " + str(str(time()-ti).replace(".", ",")))
for entativas in range(falhas):
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
    print("Top1: "+str(populacao.getTop1().getFitness()) + " | Geração: "+str(geracoes) +
          " | " + str(str(time()-ti).replace(".", ",")))
tf = time()-ti
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


# escrever_json(arraySelecao)
# escrever_json(arrayCruzamtento)

# print(carregar_json('meu_arquivo.json'))
