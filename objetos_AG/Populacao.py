from .Cromossomo import Cromossomo as C
from random import randint
from copy import deepcopy


class Populacao:
    def __init__(self, pedido, frete, tam, top1):
        self.populacao = []
        self.top1 = top1
        for id in range(tam):
            cromossomo = C()
            cromossomo.preencherCromossomo(pedido, frete)
            self.populacao.append(cromossomo)
            if(cromossomo.getFitness() < self.top1.getFitness()):
                self.top1 = cromossomo
                #print("Novo Cromossomo: "+str(cromossomo.getFitness()))

    def getTop1(self):
        return self.top1

    def getPopulacao(self):
        return self.populacao

    def setTop1(self, top1):
        self.top1 = top1

    def setPopulacao(self, populacao):
        self.populacao = populacao

    def cruzamentoMonoPonto(self, pai, mae, pedido, frete):
        ponto = pedido[randint(0, len(pedido))-1].getCarta().getId()
        filho1 = C()
        filho2 = C()
        pos = 0
        for pos in range(len(mae.getCromossomo())):
            if(int(pai.getCromossomo()[pos].getCarta().getId()) == int(ponto)):
                break
        filho1.setCromossomo(pai.getCromossomo()[
                             0:pos] + mae.getCromossomo()[pos::])
        filho2.setCromossomo(mae.getCromossomo()[
                             0:pos] + pai.getCromossomo()[pos::])
        filho1.avaliacao(frete)
        filho2.avaliacao(frete)
        if(self.top1.getFitness() > filho1.getFitness()):
            self.top1 = filho1
            #print("Filho1 " + str(filho1.getFitness())+" é melhor que o Top1")
        if(self.top1.getFitness() > filho2.getFitness()):
            self.top1 = filho2
            #print("Filho2 " + str(filho2.getFitness())+" é melhor que o Top1")
        self.populacao.append(filho1)
        self.populacao.append(filho2)

    def cruzamento(self, tam, pedido, frete):
        copiaPopulacao = deepcopy(self.populacao)
        for id in range(int(tam/2)):
            self.cruzamentoMonoPonto(
                aleatorio(copiaPopulacao), aleatorio(copiaPopulacao), pedido, frete)

    def insercao(self, pedido, frete, tam):
        for id in range(tam):
            cromossomo = C()
            cromossomo.preencherCromossomo(pedido, frete)
            self.populacao.append(cromossomo)
            if(cromossomo.getFitness() < self.top1.getFitness()):
                self.top1 = cromossomo
                #print("Novo Cromossomo: "+str(cromossomo.getFitness()))

    def mutacao(self, frete, chanceMutacao):
        for cromossomo in self.populacao:
            if(randint(0, 100) < chanceMutacao):
                mutante = deepcopy(cromossomo)
                mutante.mutacao(frete)
                self.populacao.append(mutante)
                if(mutante.getFitness() < self.top1.getFitness()):
                    self.top1 = mutante
                    #print("Mutante: "+str(mutante.getFitness()))

    def selecao(self, tam):
        self.populacao.sort(key=lambda x: x.getFitness())
        del(self.populacao[tam::])

    def toStringValor(self):
        texto = ""
        for item in self.populacao:
            texto += "Fitness: R$" + str(item.getFitness()) + ".\n"
        return texto


def aleatorio(lista):
    return lista.pop(randint(0, len(lista)-1))
