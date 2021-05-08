from threading import Thread
import time
import sys
from objetos_AG import control, Cromossomo as C, Populacao


# Criando as threads
arqFretes = control.lerArquivo("arquivos/ligamagicFrete.txt")
arqFretesTeste = control.lerArquivo("arquivos/ligamagicFreteTeste.txt")
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
# frete = control.geraVetorFrete(arqFretesTeste)
pedido = control.geraPedido(arqPedido4, arqPreco, arqQtd)

#top = ["", sys.maxsize]
th = 20
# for th in range(1, 100):
populacao = []
tamanho = 500
tam = int(tamanho / int(th))


def ini():
    for i in range(th):
        t = Thread(target=thr(tam))
        t.start()
        t.join()


def thr(tam):
    for numero in range(tam):
        cromossomo = C.Cromossomo()
        cromossomo.preencherCromossomo(pedido)
        cromossomo.avaliacao(frete)
        populacao.append(cromossomo)


tic = time.time()
ini()
toc = time.time()
texto = "Tamanho da populaçõa: " + str(len(populacao))+"\nQuantidade de Threads: "+str(
    th) + "\nTempo para processar: " + str(toc-tic)+"s."
print(texto)
'''
    if (top[1] > (toc-tic)):
        top[0] = str(texto)
        top[1] = toc-tic
        print("Melhorou:\n"+str(texto))

        
print(top[0])
'''
