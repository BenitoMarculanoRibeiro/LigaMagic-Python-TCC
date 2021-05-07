from .Cromossomo import Cromossomo
from random import randint, shuffle
import copy


class Populacao:
    def __init__(self, pedido, frete, tam, top1):
        self.populacao = []
        self.pais = []
        self.filhos = []
        for i in range(tam):
            cromossomo = Cromossomo()
            cromossomo.preencherCromossomo(pedido, frete)
            cromossomo.avaliacao(frete)
            self.populacao.append(cromossomo)
        mergeSort(self.populacao)
        if(self.populacao[0].getFitness() < top1.getFitness()):
            self.top1 = self.populacao[0]
        else:
            self.top1 = top1
        copiaPopulacao = copy.deepcopy(self.populacao)
        self.pais.append(roleta(copiaPopulacao))
        self.pais.append(roleta(copiaPopulacao))
        #print("Top1: " + str(self.top1.getFitness()) + "\nCromossomo: " + str(cromossomo.getFitness()))

    def getTop1(self):
        return self.top1

    def getPopulacao(self):
        return self.populacao

    def getPais(self):
        return self.pais

    def getFilhos(self):
        return self.filhos

    def setTop1(self, top1):
        self.top1 = top1

    def setPais(self, pai, pos):
        self.pais[pos] = pai

    def setFilhos(self, filho, pos):
        self.filhos[pos] = filho

    def setPopulacao(self, populacao):
        self.populacao = populacao

    def toStringValor(self):
        texto = ""
        for item in self.populacao:
            texto += "Fitness: R$" + str(item.getFitness()) + ".\n"
        return texto

    def cruzamentoMonoPonto(self, pedido, frete):
        ponto = pedido[randint(1, len(pedido)-2)].getCarta().getId()
        pos = 0
        status = randint(0, 1)
        for pos in range(len(self.pais[0].getCromossomo())):
            if(int(self.pais[0].getCromossomo()[pos].getCarta().getId()) == int(ponto)):
                status = 1
            if(status == 0):
                self.filhos[0].getCromossomo().append(
                    self.pais[0].getCromossomo()[pos])
                self.filhos[1].getCromossomo().append(
                    self.pais[1].getCromossomo()[pos])
            else:
                self.filhos[0].getCromossomo().append(
                    self.pais[1].getCromossomo()[pos])
                self.filhos[1].getCromossomo().append(
                    self.pais[0].getCromossomo()[pos])
            pos += 1
        self.filho.avaliacao(frete)
        if(self.top1.getFitness() > self.filho.getFitness()):
            self.top1 = self.filho

    def cruzamentoMultiPontos(self, frete):
        pos = 0
        status = randint(0, 1)
        pai = Cromossomo()
        mae = Cromossomo()
        for pos in range(len(self.pais[0].getCromossomo())-1):
            if(int(self.pais[0].getCromossomo()[pos].getCarta().getId()) != int(self.pais[0].getCromossomo()[pos-1].getCarta().getId()) or int(self.pais[0].getCromossomo()[pos-1].getCarta().getId()) == None):
                status = randint(0, 1)
            if(status == 0):
                pai.getCromossomo().append(self.pais[0].getCromossomo()[pos])
                mae.getCromossomo().append(self.pais[1].getCromossomo()[pos])
            else:
                pai.getCromossomo().append(self.pais[1].getCromossomo()[pos])
                mae.getCromossomo().append(self.pais[0].getCromossomo()[pos])
            pos += 1
        self.filhos.append(pai)
        self.filhos.append(mae)
        self.filhos[0].avaliacao(frete)
        self.filhos[1].avaliacao(frete)
        for i in self.filhos:
            #print("Top1 "+str(self.top1.getFitness()))
            #print("I "+str(i.getFitness()))
            if(self.top1.getFitness() > i.getFitness()):
                self.top1 = i
                #print("Filho " + str(i.getFitness())+" é melhor que o Top1")

    def cruzamentoMultiPontosInsercao(self, pai, mae, frete):
        pos = 0
        status = randint(0, 1)
        filho = Cromossomo()
        for pos in range(len(self.pais[0].getCromossomo())-1):
            if(int(self.pais[0].getCromossomo()[pos].getCarta().getId()) != int(self.pais[0].getCromossomo()[pos-1].getCarta().getId()) or int(self.pais[0].getCromossomo()[pos-1].getCarta().getId()) == None):
                status = randint(0, 1)
            if(status == 0):
                filho.getCromossomo().append(pai.getCromossomo()[pos])
            else:
                filho.getCromossomo().append(mae.getCromossomo()[pos])
            pos += 1
        filho.avaliacao(frete)
        for i in self.filhos:
            if(self.top1.getFitness() > i.getFitness()):
                self.top1 = i
                #print("Filho " + str(i.getFitness())+" é melhor que o Top1")
        self.populacao.append(filho)

    def insercao(self, pedido, frete, tam, top1):
        self.populacao = []
        for i in range(tam):
            status = randint(0, 1)
            if(status == 0):
                cromossomo = Cromossomo()
                cromossomo.preencherCromossomo(pedido, frete)
                self.cruzamentoMultiPontosInsercao(
                    cromossomo, self.pais[0], frete)
            else:
                cromossomo = Cromossomo()
                cromossomo.preencherCromossomo(pedido, frete)
                self.cruzamentoMultiPontosInsercao(
                    cromossomo, self.pais[1], frete)
        mergeSort(self.populacao)
        if(self.populacao[0].getFitness() < top1.getFitness()):
            self.top1 = self.populacao[0]
        else:
            self.top1 = top1
        copiaPopulacao = copy.deepcopy(self.populacao)
        self.setPais(roleta(copiaPopulacao),0)
        self.setPais(roleta(copiaPopulacao),1)


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i].getFitness() < righthalf[j].getFitness():
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1


def roleta(lista):
    vetor = []
    cont = len(lista)
    for i in lista:
        for j in range(cont):
            vetor.append(i)
        cont -= 1
    shuffle(vetor)
    result = vetor.pop(0)
    return result
