from .Cromossomo import Cromossomo as C
from threading import Thread
from random import randint, shuffle
import copy


class Populacao:
    tam = 0

    def __init__(self, pedido, frete, tam, top1, aux):
        self.populacao = []
        self.pais = []
        self.filhos = []
        num = 10
        tam
        div = int(tam/num)
        resto = int(tam % num)
        for id in range(num):
            if(id == (num-1)):
                t = Thread(target=self.thr(div+resto, pedido, frete, aux))
                t.start()
                t.join()
            else:
                t = Thread(target=self.thr(div, pedido, frete, aux))
                t.start()
                t.join()
        # print(len(self.populacao))
        copiaPopulacao = copy.deepcopy(self.populacao)
        mergeSort(self.populacao)
        if(self.populacao[0].getFitness() < top1.getFitness()):
            self.top1 = self.populacao[0]
            self.pais.append(roleta1(copiaPopulacao))
            self.pais.append(roleta1(copiaPopulacao))
        else:
            self.top1 = top1
            self.pais.append(roleta(copiaPopulacao, self.top1))
            self.pais.append(roleta(copiaPopulacao, self.top1))
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

    def thr(self, tam, pedido, frete, aux):
        for i in range(tam):
            cromossomo = C()
            cromossomo.preencherCromossomo(pedido, frete, aux)
            cromossomo.avaliacao(frete)
            self.populacao.append(cromossomo)

    def thrInsercao(self, tam, pedido, frete, top1, aux):
        for i in range(tam):
            cromossomo = C()
            cromossomo.preencherCromossomo(pedido, frete, aux)
            status = randint(0, 2)
            if(status == 0):
                self.cruzamentoMultiPontosInsercao(cromossomo, top1, frete)
            elif(status == 1):
                self.cruzamentoMultiPontosInsercao(
                    cromossomo, self.pais[0], frete)
            else:
                self.cruzamentoMultiPontosInsercao(
                    cromossomo, self.pais[1], frete)
            self.populacao.append(cromossomo)

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

    def cruzamentoMonoPonto1(self, pedido, frete):
        ponto = pedido[randint(1, len(pedido)-2)].getCarta().getId()
        pos = 0
        status = randint(0, 1)
        pai = C()
        mae = C()
        for pos in range(len(self.pais[0].getCromossomo())):
            if(int(self.pais[0].getCromossomo()[pos].getCarta().getId()) == int(ponto)):
                status = 1
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

    def cruzamentoMonoPonto1Insercao(self, pai, mae, pedido, frete):
        ponto = pedido[randint(1, len(pedido)-2)].getCarta().getId()
        pos = 0
        status = randint(0, 1)
        filho = C()
        for pos in range(len(self.pais[0].getCromossomo())):
            if(int(self.pais[0].getCromossomo()[pos].getCarta().getId()) == int(ponto)):
                status = 1
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

    def cruzamentoMultiPontos(self, frete):
        pos = 0
        status = randint(0, 1)
        pai = C()
        mae = C()
        # for pos in range(len(self.pais[0].getCromossomo())-1):
        for pos in range(len(self.pais[0].getCromossomo())):
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
        filho = C()
        # for pos in range(len(self.pais[0].getCromossomo())-1):
        for pos in range(len(self.pais[0].getCromossomo())):
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

    def insercao(self, pedido, frete, tam, top1, aux):
        self.populacao = []
        num = 10
        tam
        div = int(tam/num)
        resto = int(tam % num)
        for id in range(num):
            if(id == (num-1)):
                t = Thread(target=self.thrInsercao(
                    div+resto, pedido, frete, top1, aux))
                t.start()
                t.join()
            else:
                t = Thread(target=self.thrInsercao(
                    div, pedido, frete, top1, aux))
                t.start()
                t.join()
        mergeSort(self.populacao)
        if(self.populacao[0].getFitness() < top1.getFitness()):
            self.top1 = self.populacao[0]
            copiaPopulacao = copy.deepcopy(self.populacao)
            self.setPais(roleta1(copiaPopulacao), 0)
            self.setPais(roleta1(copiaPopulacao), 1)
        else:
            self.top1 = top1
            copiaPopulacao = copy.deepcopy(self.populacao)
            self.setPais(roleta(copiaPopulacao, self.top1), 0)
            self.setPais(roleta(copiaPopulacao, self.top1), 1)


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


def roleta(lista, top1):
    vetor = []
    cont = len(lista)
    for i in lista:
        for j in range(cont):
            vetor.append(i)
        cont -= 1
    for i in range(cont+1):
        vetor.append(top1)
    shuffle(vetor)
    result = vetor.pop(0)
    return result


def roleta1(lista):
    vetor = []
    cont = len(lista)
    for i in lista:
        for j in range(cont):
            vetor.append(i)
        cont -= 1
    shuffle(vetor)
    result = vetor.pop(0)
    return result
