from cromossomo import Cromossomo

class Populacao:
    def __init__(self, pedido, frete, tam):
        self.populacao = []
        self.top1 = None
        for i in range(tam):
            cromossomo = Cromossomo()
            cromossomo.preencherCromossomo(pedido, frete)
            self.populacao.append(cromossomo)
            if(self.top1 == None or self.top1.getFitness() > cromossomo.getFitness()):
                self.top1 = cromossomo
            #print("Top1: " + str(self.top1.getFitness()) + "\nCromossomo: " + str(cromossomo.getFitness()))

    def getTop1(self):
        return self.top1

    def getPopulacao(self):
        return self.populacao

    def setTop1(self, top1):
        self.top1 = top1

    def setPopulacao(self, populacao):
        self.populacao = populacao

    def toStringValor(self):
        texto = ""
        for item in self.populacao:
            texto += "Fitness: R$" + str(item.getFitness()) + ".\n"
        return texto