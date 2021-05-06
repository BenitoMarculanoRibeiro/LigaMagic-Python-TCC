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


    def cruzamentoMultiPontosInsercao(self, pai, aleatorio, frete):
        pos = 0
        status = 0
        filho1 = Cromossomo()
        filho2 = Cromossomo()
        for pos in range(len(self.pais[0].getCromossomo())-1):
            if(int(self.pais[0].getCromossomo()[pos].getCarta().getId()) != int(self.pais[0].getCromossomo()[pos-1].getCarta().getId()) or int(self.pais[0].getCromossomo()[pos-1].getCarta().getId()) == None):
                status = random.randint(0, 1)
            if(status == 0):
                filho1.getCromossomo().append(pai.getCromossomo()[pos])
                filho2.getCromossomo().append(aleatorio.getCromossomo()[pos])
            else:
                filho1.getCromossomo().append(aleatorio.getCromossomo()[pos])
                filho2.getCromossomo().append(pai.getCromossomo()[pos])
            pos += 1
        filhos = []
        filhos.append(filho1)
        filhos.append(filho2)
        filhos[0].avaliacao(frete)
        filhos[1].avaliacao(frete)
        for i in self.filhos:
            if(self.top1.getFitness() > i.getFitness()):
                self.top1 = i
                print("Filho "+ str(i.getFitness())+" é melhor que o Top1")
