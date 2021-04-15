# arquivo para armazenar codigos que podem voltar a serem usados

def lerPedido(caminho):
    pedido = []
    l = []
    c = []
    f = open(caminho, 'r')
    for line in f:
        linha = line.split()
        l.append(linha[0])
        c.append(linha[1])
    pedido.append(l)
    pedido.append(c)
    return pedido


class Card:
    ativo = False

    def __init__(self, nome, vetPreco, vetQtd) -> None:
        self.nome = nome
        self.vetPreco = vetPreco
        self.vetQtd = vetQtd

    def clone(self):
        cardClone = Card(self.nome, self.vetPreco, self.vetQtd)
        return cardClone


def selecionarCartaLojaValido(id, vetCartas, vetUsados):
    loja = random.randint(0, vetCartas[id])

    if(len(vetUsados) != len(vetCartas[id])):
        if (vetCartas[id][loja] > 0):
            return loja
        else:
            vetUsados.append(loja)
            lo = selecionarCartaLojaValido(id, vetCartas, vetUsados)
            return lo
    return selecionarCartaLojaValido(id, vetCartas, vetUsados)


def pedido(vetPedido):
    pedido = []
    listaPedido = listaIdPedido(vetPedido)
    for id in listaPedido:
        pedidoStatus = Pedido()
        pedidoStatus.setCarta(id[0])
        pedidoStatus.setQtd(id[1])
        pedido.append(pedidoStatus)
    return pedido


def frete(vetFrete):
    vetFrete[1].pop(0)
    return vetFrete[1]


for carta in vetPedido:
    print(str(carta.getCarta()) + " - " + str(carta.getQtd()))


for carta in vetCartas:
    print(str(carta.getId()) + " - " + str(carta.getNome()) + " - " +
          str(carta.getPrecos()) + " - " + str(carta.getQtd()))
