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

    def mais1(self, i):
        self.vetQtd[i] = int(self.vetQtd[i]) + 1

    def menos1(self, i):
        self.vetQtd[i] = int(self.vetQtd[i]) - 1

    def toString(self):
        return str("Id Carta: " + str(self.getId()) + "\nNome: " + str(self.getNome()) + "\nVetor de Precos: \n" + str(self.getPrecos()) + " \nVetor de Quantidade: \n" + str(self.getQtd()) + " \n\n")
