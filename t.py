from threading import Thread, Lock
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
soma = 0
populacao = []
# O objeto responsável por ler e anotar os resultados


class LeitorTXT(Thread):
    def __init__(self, qtd, ident, mutex):
        self.qtd = qtd
        self.id = ident
        self.locker = mutex
        self.soma = 0

        Thread.__init__(self)

    def run(self):
        global Resultados
        for numero in range(self.qtd):
            cromossomo = C.Cromossomo()
            cromossomo.preencherCromossomo(pedido)
            cromossomo.avaliacao(frete)
            populacao.append(cromossomo)
            Resultados.append(self.soma)


Resultados = []
TodasThreads = []


# num == Numero de threads
# linhas == Quantidade de linhas do txt
# locker == Ao locker que bloqueia e desbloqueia as threads

num = 4
tamanho = 101 
div = int(tamanho/num)
resto =int(tamanho%num)
print(tamanho)
print(div)
print(resto)
locker = Lock()
for id in range(num):
    if(id == (num-1)):
        thread = LeitorTXT((div+resto), id, locker)
    else:
        thread = LeitorTXT(div, id, locker)
    # A fórmula é simples
    # linhas do txt dividido pelo número de threads → Mesma quantidade pra cada uma.
    # Multiplicadas pelo o id, pq como é número:
    # A 1 (id == 0) thread lê as primeiras 250k linhas
    # A 2 (id == 1) thread lê as seguintes 250k (250k anterior)
    # A 3 (id == 2) thread lê as seguintes 250 (250k + 250k das anteriores)
    # e daí em diante

    thread.start()
    TodasThreads.append(thread)

for thread in TodasThreads:
    thread.join()

print('Resultado final:', len(Resultados))
