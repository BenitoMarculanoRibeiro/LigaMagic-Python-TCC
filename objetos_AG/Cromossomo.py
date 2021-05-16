from .Gene import Gene
from random import randint, sample
from copy import deepcopy


class Cromossomo:
    def __init__(self):
        self.cromossomo = []
        self.fitness = None

    def getCromossomo(self):
        return self.cromossomo

    def getFitness(self):
        return self.fitness

    def setCromossomo(self, cromossomo):
        self.cromossomo = cromossomo

    def setFitness(self, fitness):
        self.fitness = fitness

    def preencherCromossomo(self, pedido, frete):
        copiaPedido = deepcopy(pedido)
        for item in copiaPedido:
            aux = sample(range(0, len(item.getCarta().getQtd())),
                         len(item.getCarta().getQtd()))
            for j in range(int(item.getQtd())):
                for i in aux:
                    try:
                        if(int(item.getCarta().getQtd()[i]) > 0):
                            gene = Gene()
                            gene.setCarta(item.getCarta())
                            gene.setLoja(i)
                            item.getCarta().menos1(i)
                            self.cromossomo.append(gene)
                            break
                    except:
                        print("Erro preencherCromossomo")
                        pass
                    if(i == aux[-1]):
                        print("Acabou a carta: " +
                              str(item.getCarta().getNome())) + ". Pedido Invalido."
                        return False
        self.avaliacao(frete)

    def avaliacao(self, frete):
        fitness = 0
        vetLoja = []
        for gen in self.cromossomo:
            fitness += float(gen.getCarta().getPrecos()[gen.getLoja()])
            if gen.getLoja() not in vetLoja:
                fitness += float(frete[gen.getLoja()].getFrete())
                vetLoja.append(gen.getLoja())
        self.fitness = round(fitness, 2)

    def retornaAvaliacao(self, frete):
        fitness = 0
        vetLoja = []
        for gen in self.cromossomo:
            fitness += float(gen.getCarta().getPrecos()[gen.getLoja()])
            if gen.getLoja() not in vetLoja:
                fitness += float(frete[gen.getLoja()].getFrete())
                vetLoja.append(gen.getLoja())
        return round(fitness, 2)

    def mutacao(self, frete):
        if(len(self.cromossomo) > 0):
            gene = self.cromossomo[randint(0, len(self.cromossomo)-1)]
            gene.getCarta().mais1(gene.getLoja())
            posLoja = randint(0, len(gene.getCarta().getQtd())-1)
            loja = gene.getCarta().getQtd()[posLoja]
            if(int(loja) > 0):
                gene.setLoja(posLoja)
                gene.getCarta().menos1(posLoja)
                self.avaliacao(frete)
                # print("Mutou")
            # else:
                # mutação falhou por falta de carta na loja
        # else:
            # mutação não vai acontecer por falta de chance

    def toString(self):
        texto = ""
        for i in self.cromossomo:
            texto += str(i.toString())
        texto += "Fitness: " + str(self.fitness) + "\n"
        return texto
