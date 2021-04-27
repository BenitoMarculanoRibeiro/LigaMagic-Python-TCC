class Gene:
    def __init__(self):
        self.carta = None
        self.loja = None

    def getCarta(self):
        return self.carta

    def setCarta(self, carta):
        self.carta = carta

    def getLoja(self):
        return self.loja

    def setLoja(self, loja):
        self.loja = loja

    def toString(self):
        return "Carta: " + str(self.carta.getNome()) + "\nId Loja: " + str(self.loja) + "\n"