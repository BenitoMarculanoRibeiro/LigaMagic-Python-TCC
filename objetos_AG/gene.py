# Nota: a classe Gene seria o gene
class Gene:
    def __init__(self):
        self.carta = None
        # Nota: a loja seria o alelo
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
        return "Id Loja: " + str(self.loja) + " | Carta: " + str(self.carta.getNome()) + "\n"
