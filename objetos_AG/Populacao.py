from .Cromossomo import Cromossomo
import random
import copy


class Populacao:
    def __init__(self, pedido, frete, tam, top1):
        self.populacao = []
        self.pais = []
        for i in range(tam):
            cromossomo = Cromossomo()
            cromossomo.preencherCromossomo(pedido, frete)
            self.populacao.append(cromossomo)
        mergeSort(self.populacao)
        if(top1.getFitness() == None or self.populacao[0].getFitness() < top1.getFitness()):
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

    def setTop1(self, top1):
        self.top1 = top1

    def setPopulacao(self, populacao):
        self.populacao = populacao

    def toStringValor(self):
        texto = ""
        for item in self.populacao:
            texto += "Fitness: R$" + str(item.getFitness()) + ".\n"
        return texto


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
    random.shuffle(vetor)
    result = vetor.pop(0)
    return result
