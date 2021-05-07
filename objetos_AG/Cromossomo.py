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

    def preencherCromossomo(self, pedido):
        copiaPedido = copy.deepcopy(pedido)
        for item in copiaPedido:
            vet = []
            for i in range(len(copiaPedido[0].getCarta().getPrecos())):
                vet.append(i)
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
        if(random.randint(0, 100) < chance and len(self.cromossomo)>0):
            #print(len(self.cromossomo))
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
