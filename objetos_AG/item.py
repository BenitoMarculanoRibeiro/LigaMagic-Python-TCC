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
        return str(str(self.getCarta().toString()) + " Quantidade: " + str(self.getQtd())+"\n")



