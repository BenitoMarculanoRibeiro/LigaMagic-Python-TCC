from .Cromossomo import Cromossomo as C
from threading import Thread
from random import randint, shuffle
import copy


class Populacao:
    tam = 0

    def __init__(self, pedido, frete, tam, top1, aux):
        self.populacao = []
        self.pais = [C(), C()]
        self.filhos = []
        self.top1 = top1
        for id in range(tam):
            cromossomo = C()
            cromossomo.preencherCromossomo(pedido, frete, aux)
            self.populacao.append(cromossomo)
            if(cromossomo.getFitness() < self.top1.getFitness()):
                self.top1 = cromossomo
                print("Novo Cromossomo: "+str(cromossomo.getFitness()))
            if(cromossomo.getFitness() < self.top1.getFitness()):
                self.top1 = cromossomo
                print("novo Cromossomo: "+str(cromossomo.getFitness()))

        copiaPopulacao = copy.deepcopy(self.populacao)
        self.setPais(aleatorio(copiaPopulacao), 0)
        self.setPais(aleatorio(copiaPopulacao), 1)
        '''
        num = 20
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
        # print("Top1: " + str(self.top1.getFitness()) + "\nCromossomo: " + str(cromossomo.getFitness()))
        '''

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
    '''
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
                self.cruzamentoMonoPonto1Insercao(
                    cromossomo, top1, pedido, frete)
            elif(status == 1):
                self.cruzamentoMonoPonto1Insercao(
                    cromossomo, self.pais[0], pedido, frete)
            else:
                self.cruzamentoMonoPonto1Insercao(
                    cromossomo, self.pais[1], pedido, frete)
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
            # print("Top1 "+str(self.top1.getFitness()))
            # print("I "+str(i.getFitness()))
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
                # print("Filho " + str(i.getFitness())+" é melhor que o Top1")
        self.populacao.append(filho)
    '''

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
            # print("Top1 "+str(self.top1.getFitness()))
            # print("I "+str(i.getFitness()))
            if(self.top1.getFitness() > i.getFitness()):
                self.top1 = i
                # print("Filho " + str(i.getFitness())+" é melhor que o Top1")

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
                # print("Filho " + str(i.getFitness())+" é melhor que o Top1")
        self.populacao.append(filho)

    def cruzamentoMonoPonto(self, pai, mae, pedido, frete):
        ponto = pedido[randint(1, len(pedido)-2)].getCarta().getId()
        status = 0
        filho1 = C()
        filho2 = C()
        for pos in range(len(mae.getCromossomo())):
            if(int(pai.getCromossomo()[pos].getCarta().getId()) == int(ponto)):
                status = 1
            if(status == 0):
                filho1.getCromossomo().append(pai.getCromossomo()[pos])
                filho2.getCromossomo().append(mae.getCromossomo()[pos])
            else:
                # print(filho1.toString())
                filho1.getCromossomo().append(mae.getCromossomo()[pos])
                filho2.getCromossomo().append(pai.getCromossomo()[pos])
        filho1.avaliacao(frete)
        filho2.avaliacao(frete)
        if(self.top1.getFitness() > filho1.getFitness()):
            self.top1 = filho1
            print("Filho1 " + str(filho1.getFitness())+" é melhor que o Top1")
        if(self.top1.getFitness() > filho2.getFitness()):
            self.top1 = filho2
            print("Filho2 " + str(filho2.getFitness())+" é melhor que o Top1")
        self.populacao.append(filho1)
        self.populacao.append(filho2)

    def insercao(self, pedido, frete, tam, top1, aux, taxa):
        copiaPopulacao = copy.deepcopy(self.populacao)
        self.populacao = []
        self.top1 = top1
        repro = int(tam*taxa)
        inser = tam-(repro)
        for id in range(repro):
            self.cruzamentoMonoPonto(
                aleatorio(copiaPopulacao), aleatorio(copiaPopulacao), pedido, frete)
        #print(len(self.populacao))
        for id in range(inser):
            cromossomo = C()
            cromossomo.preencherCromossomo(pedido, frete, aux)
            self.populacao.append(cromossomo)
            if(cromossomo.getFitness() < self.top1.getFitness()):
                self.top1 = cromossomo
                print("Novo Cromossomo: "+str(cromossomo.toString()))
        copiaPopulacao = copy.deepcopy(self.populacao)
        mergeSort(self.populacao)
        self.setPais(roleta(copiaPopulacao), 0)
        self.setPais(roleta(copiaPopulacao), 1)
        
    def insercao2(self, pedido, frete, tam, top1, aux):
        copiaPopulacao = copy.deepcopy(self.populacao)
        self.top1 = top1
        for id in range(int(tam/2)):
            self.cruzamentoMonoPonto(
                aleatorio(copiaPopulacao), aleatorio(copiaPopulacao), pedido, frete)
        #print(len(self.populacao))
        for id in range(tam):
            cromossomo = C()
            cromossomo.preencherCromossomo(pedido, frete, aux)
            self.populacao.append(cromossomo)
            if(cromossomo.getFitness() < self.top1.getFitness()):
                self.top1 = cromossomo
                print("Novo Cromossomo: "+str(cromossomo.getFitness()))
        #print(len(self.populacao))
        mergeSort(self.populacao)
        del(self.populacao[tam::])
        #print(len(self.populacao))
        copiaPopulacao = copy.deepcopy(self.populacao)
        self.setPais(roleta(copiaPopulacao), 0)
        self.setPais(roleta(copiaPopulacao), 1)
    
    def insercao3(self, pedido, frete, tam, top1, aux):
        self.top1 = top1
        copiaPopulacao = copy.deepcopy(self.populacao)
        for id in range(int(tam/2)):
            self.cruzamentoMonoPonto(
                aleatorio(copiaPopulacao), aleatorio(copiaPopulacao), pedido, frete)
            #print(len(self.populacao))
        for id in range(tam):
            cromossomo = C()
            cromossomo.preencherCromossomo(pedido, frete, aux)
            self.populacao.append(cromossomo)
            if(cromossomo.getFitness() < self.top1.getFitness()):
                self.top1 = cromossomo
                print("Novo Cromossomo: "+str(cromossomo.getFitness()))
        #print(len(self.populacao))
        print(self.toStringValor())
        print(len(self.populacao))
        mergeSort(self.populacao)
        print(len(self.populacao))
        print(self.toStringValor())
        del(self.populacao[tam::])
        print(len(self.populacao))
        print(self.toStringValor())
    '''
    def insercao(self, pedido, frete, tam, top1, aux):
        self.populacao = []
        self.top1 = top1
        for id in range(tam):
            cromossomo = C()
            cromossomo.preencherCromossomo(pedido, frete, aux)
            self.populacao.append(cromossomo)
            if(cromossomo.getFitness() < self.top1.getFitness()):
                self.top1 = cromossomo
                print("Novo Cromossomo:\n"+str(cromossomo.toString())+"\n")
            status = randint(0, 2)
            if(status == 0):
                self.cruzamentoMonoPonto(
                    cromossomo, self.top1, pedido, frete)
            elif(status == 1):
                self.cruzamentoMonoPonto(
                    cromossomo, self.pais[0], pedido, frete)
            else:
                self.cruzamentoMonoPonto(
                    cromossomo, self.pais[1], pedido, frete)
            # self.populacao.append(cromossomo)
            if(cromossomo.getFitness() < self.top1.getFitness()):
                self.top1 = cromossomo
                print("Inserção:\n"+str(cromossomo.toString())+"\n")
        print(len(self.populacao))
        copiaPopulacao = copy.deepcopy(self.populacao)
        self.setPais(aleatorio(copiaPopulacao), 0)
        self.setPais(aleatorio(copiaPopulacao), 1)



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

    '''


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


def aleatorio(lista):
    return lista.pop(randint(0, len(lista)-1))





def roleta(lista):
    vetor = []
    cont = len(lista)
    for i in lista:
        for j in range(cont):
            vetor.append(i)
        cont -= 1
    shuffle(vetor)
    return vetor.pop(0)
