from .gene import Gene
import random
import copy


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
        copiaPedido = copy.deepcopy(pedido)
        for item in copiaPedido:
            vet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
                   44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]
            random.shuffle(vet)
            for j in range(int(item.getQtd())):
                for i in vet:
                    try:
                        loja = item.getCarta().getQtd()[i]
                        if(int(loja) > 0):
                            #print("Id Carta: "+str(item.getCarta().getId()) + " Posicao " + str(i) + " qtd: " + str(loja))
                            gene = Gene()
                            gene.setCarta(item.getCarta())
                            gene.setLoja(i)
                            #print("Qtd Antes: " + str(item.getCarta().getQtd()[i]))
                            item.getCarta().menos1(i)
                            #print("Qtd Depois: " + str(item.getCarta().getQtd()[i])+"\n")
                            self.cromossomo.append(gene)
                            # print(gene.toString())
                            break
                    except:
                        print("Aviso " + str(loja)+", tipo: " +
                              str(type(loja) is int))
                        pass
                    if(i == vet[-1]):
                        print("Acabou a carta: " +
                              str(item.getCarta().getNome())) + ". Pedido Invalido."
                        return False

    def avaliacao(self, frete):
        fitness = 0
        vetLoja = []
        for gen in self.cromossomo:
            #print("Carta" +str(gen.getCarta().getNome())+"Preco Carta: " + str(float(gen.getCarta().getPrecos()[gen.getLoja()])))
            fitness += float(gen.getCarta().getPrecos()[gen.getLoja()])
            if gen.getLoja() not in vetLoja:
                #print("Preco Frete: " + str(float(frete.getFrete(gen.getLoja()).getFrete()))+ " Loja: " + str(gen.getLoja()))
                fitness += float(frete[gen.getLoja()].getFrete())
                vetLoja.append(gen.getLoja())
        self.fitness = round(fitness, 2)

    def retornaAvaliacao(self, frete):
        fitness = 0
        vetLoja = []
        for gen in self.cromossomo:
            #print("Carta" +str(gen.getCarta().getNome())+"Preco Carta: " + str(float(gen.getCarta().getPrecos()[gen.getLoja()])))
            fitness += float(gen.getCarta().getPrecos()[gen.getLoja()])
            if gen.getLoja() not in vetLoja:
                #print("Preco Frete: " + str(float(frete.getFrete(gen.getLoja()).getFrete()))+ " Loja: " + str(gen.getLoja()))
                fitness += float(frete[gen.getLoja()].getFrete())
                vetLoja.append(gen.getLoja())
        return round(fitness, 2)

    def mutacao(self, frete, chance):
        if(random.randint(0, 100) < chance):
            gene = self.cromossomo[random.randint(0, len(self.cromossomo)-1)]
            gene.getCarta().mais1(gene.getLoja())
            posLoja = random.randint(0, len(gene.getCarta().getQtd())-1)
            loja = gene.getCarta().getQtd()[posLoja]
            if(int(loja) > 0):
                gene.setLoja(posLoja)
                gene.getCarta().menos1(posLoja)
            # else:
                # mutação falhou por falta de carta na loja
        # else:
            # mutação não vai acontecer por falta de chance
        self.avaliacao(frete)

    def toString(self):
        texto = ""
        for i in self.cromossomo:
            texto += str(i.toString())
        texto += "Fitness: " + str(self.fitness) + "\n"
        return texto
