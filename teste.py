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
pedido = control.geraPedido(arqPedido1, arqPreco, arqQtd)
arqPreco.clear()
arqQtd.clear()
#pedido = control.geraPedido(arqPedidoTeste, arqPrecoTeste, arqQtdTeste)
# geracoes serve para saber quantas gerações de populações foram rodadas
geracoes = 0
# cont conta as falhas
cont = 0
# tam é o tamnho da população
tam = 10
# falhas são quantas falhas podem ocorrer sem que seja adquirido algum cromossomo mais barato
falhas = 100
# tempo é por quanto tempo quer rodar o programa em segundos
tempo = 360
# Chance de ocorrer mutação, é bom 1 = 1%
chanceMutacao = 3
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
populacao.insercao3(pedido, frete, tam, top1, aux)
populacao.insercao3(pedido, frete, tam, top1, aux)
