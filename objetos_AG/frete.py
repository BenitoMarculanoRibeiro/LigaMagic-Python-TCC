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
