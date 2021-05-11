from .item import Item
from .carta import Carta
from .frete import Frete

def lerArquivo(caminho):
    vet = []
    for line in open(caminho, 'r'):
        c = []
        linha = line.split("	")
        for collun in linha:
            c.append(collun)
        vet.append(c)
    return vet


def lerArquivo2(caminho):
    vet = []
    f = open(caminho, 'r')
    for line in f:
        c = []
        linha = line.split("|")
        for collun in linha:
            collun = collun.rstrip("\n")
            c.append(collun)
        vet.append(c)
    return vet


def toStringPedido(pedido):
    texto = ""
    for item in pedido:
        texto += item.toString()
    return texto


def tamanhoPedido(pedido):
    return len(pedido)


def geraPedido(vetPedido, vetPrecos, vetQtds):
    pedido = []
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
        pedido.append(pedidoStatus)
    return pedido

def geraVetorFrete(vetFrete):
    vetFrete[1].pop(0)
    fretes = []
    for i in vetFrete[1]:
        frete = Frete()
        frete.setLoja(vetFrete[1].index(i))
        frete.setFrete(vetFrete[1][vetFrete[1].index(i)])
        fretes.append(frete)
    return fretes


def toStringFrete(fretes):
    texto = ""
    for i in fretes:
        texto += "Loja " + str(i.getLoja()) + " - " + str(i.getFrete()) + "\n"
    return texto
