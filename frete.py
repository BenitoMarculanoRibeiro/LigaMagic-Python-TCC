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

    def toString(self):
        return "Loja "+str(self.getLoja())+": "+str(self.getFrete())+"\n"


def geraVetorFrete(vetFrete):
    vetFrete[1].pop(0)
    fretes = []
    for i in vetFrete[1]:
        frete = Frete()
        frete.setLoja(vetFrete[1].index(i))
        frete.setFrete(vetFrete[1][vetFrete[1].index(i)])
        fretes.append(frete)
    return fretes


def toString(fretes):
    texto = ""
    for i in fretes:
        texto += "Loja " + str(i.getLoja()) + " - " + str(i.getFrete()) + "\n"
    return texto
