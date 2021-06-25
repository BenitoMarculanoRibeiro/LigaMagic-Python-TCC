# coding: utf-8
from objetos_AG import Control as c, Cromossomo, Populacao
from time import time

# Recebendo dados dos arquivos
arqFretes = c.lerArquivo("arquivos/ligamagicFrete.txt")
arqPedido = c.lerArquivo("arquivos/ligamagicPedido4.txt")
arqPreco = c.lerArquivo("arquivos/ligamagicPreco.txt")
arqQtd = c.lerArquivo("arquivos/ligamagicQtd.txt")
# frete é uma variavel que com os valores de frete por loja
frete = c.geraVetorFrete(arqFretes)
#frete = c.geraVetorFrete(arqFretesTeste)
# pedido contem um Id, nome, vetor de preço por loja e vetor de quantidade por loja
pedido = c.geraPedido(arqPedido, arqPreco, arqQtd)
arqPreco.clear()
arqQtd.clear()
top1 = Cromossomo.Cromossomo()
    # Iniciando o Top1 com o valor do maior int possivel para que ao ser analisado posteriormente seja excluido
top1.preencherCromossomo(pedido, frete)
#pedido = c.geraPedido(arqPedidoTeste, arqPrecoTeste, arqQtdTeste)
# geracoes serve para saber quantas gerações de populações foram rodadas
print(len(top1.getCromossomo()))
print(top1)