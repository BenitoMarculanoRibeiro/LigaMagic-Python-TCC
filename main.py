import random


class Carta:
    def __init__(self):
        self.id = None
        self.nome = None
        self.vetPreco = None
        self.vetQtd = None

    def getCarta(vetCarta, id):
        return vetCarta[id]

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getPrecos(self):
        return self.vetPreco

    def getQtd(self):
        return self.vetQtd

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setPrecos(self, vetPreco):
        self.vetPreco = vetPreco

    def setQtd(self, vetQtd):
        self.vetQtd = vetQtd


class Item:

    def __init__(self):
        self.carta = None
        self.qtd = None

    def getCarta(self):
        return self.carta

    def setCarta(self, carta):
        self.carta = carta

    def getQtd(self):
        return self.qtd

    def setQtd(self, qtd):
        self.qtd = qtd

    def decaiQtd(self):
        self.qtd -= 1

    def toString(self):
        return "Id Carta: " + str(self.getCarta()) + " Quantidade: " + str(self.getQtd())


class Frete:
    def __init__(self):
        self.loja = None
        self.frete = None

    def getLoja(self):
        return self.loja

    def setLoja(self, loja):
        self.loja = loja

    def getFrete(self):
        return self.frete

    def setFrete(self, frete):
        self.frete = frete


class Fretes:
    def __init__(self):
        self.fretes = []

    def getFrete(self, id):
        self

    def geraVetorFrete(self, vetFrete):
        vetFrete[1].pop(0)
        for i in vetFrete[1]:
            frete = Frete()
            frete.setLoja(vetFrete[1].index(i))
            frete.setFrete(vetFrete[1])
            self.fretes.append(frete)


class Pedido:
    def __init__(self):
        self.pedido = []

    def getPedido(self):
        return self.pedido

    def setPedido(self, pedido):
        self.pedido = pedido

    def toString(self):
        texto = ""
        for item in self.pedido:
            texto += item.toString()
        return texto

    def tamanhoPedido(self):
        return len(self.pedido)

    def geraPedido(self, vetPedido, vetPrecos, vetQtds):
        for id in vetPedido:
            nome = vetPrecos[int(id[0])].pop(0)
            vetQtds[int(id[0])].pop(0)
            carta = Carta()
            carta.setId(int(id[0]))
            carta.setNome(nome)
            carta.setPrecos(vetPrecos[int(id[0])])
            carta.setQtd(vetQtds[int(id[0])])
            pedidoStatus = Item()
            pedidoStatus.setCarta(carta)
            pedidoStatus.setQtd(id[1])
            self.pedido.append(pedidoStatus)


class Gene:
    def __init__(self):
        self.id
        self.loja

    def __init__(self, id, loja):
        self.id = id
        self.loja = loja

    def getId(self):
        return self.id

    def getLoja(self):
        return self.loja


class Cromossomo:
    def __init__(self):
        self.cromossomo = None
        self.fitness = None

    def preencherCromossomo(self, vetCartas, pedido):
        for item in pedido.getPedido():
            print(item.getCarta())
        pass

    def calculaFitness(self):
        pass


def lerArquivo(caminho):
    vet = []
    f = open(caminho, 'r')
    for line in f:
        c = []
        linha = line.split("	")
        for collun in linha:
            c.append(collun)
        vet.append(c)
    return vet


def listaIdPedido(vetPedido):
    listaPedido = []
    for item in vetPedido:
        listaPedido.append([int(item[0]), int(item[1])])
    return listaPedido


def cartas(vetPedido, vetPrecos, vetQtds):
    vetCards = []
    for id in vetPedido:
        nome = vetPrecos[int(id[0])].pop(0)
        vetQtds[int(id[0])].pop(0)
        carta = Carta()
        carta.setId(int(id[0]))
        carta.setNome(nome)
        carta.setPrecos(vetPrecos[int(id[0])])
        carta.setQtd(vetQtds[int(id[0])])
        vetCards.append(carta)
    return vetCards


def toStringArrayCartas(vetCartas):
    texto = ""
    for carta in vetCartas:
        texto += str("Id Carta: " + str(carta.getId()) + "\nNome: " + str(carta.getNome()) +
                     "\nVetor de Precos: \n" + str(carta.getPrecos()) + " \nVetor de Quantidades: \n" + str(carta.getQtd()) + " \n\n")
    return texto


vetFretes = lerArquivo("arquivos/ligamagicFrete.txt")
pedido1 = lerArquivo("arquivos/ligamagicPedido1.txt")
pedido2 = lerArquivo("arquivos/ligamagicPedido2.txt")
pedido3 = lerArquivo("arquivos/ligamagicPedido3.txt")
pedido4 = lerArquivo("arquivos/ligamagicPedido4.txt")
vetPreco = lerArquivo("arquivos/ligamagicPreco.txt")
vetQtd = lerArquivo("arquivos/ligamagicQtd.txt")
'''
vetCartas = cartas(pedido1, vetPreco, vetQtd)
print(len(vetCartas))
'''
vetPedido = Pedido()
vetPedido.geraPedido(pedido1, vetPreco, vetQtd)
print(len(vetPedido.getPedido()))
frete = Fretes()
frete.geraVetorFrete(vetFretes)
cromossomo = Cromossomo()
cromossomo.preencherCromossomo(vetPedido)