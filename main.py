import random
import copy


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
        self.vetQtd[i] += 1

    def menos1(self, i):
        self.vetQtd[i] = int(self.vetQtd[i]) - 1

    def toString(self):
        return str("Id Carta: " + str(self.getId()) + "\nNome: " + str(self.getNome()) + "\nVetor de Precos: \n" + str(self.getPrecos()) + " \nVetor de Quantidade: \n" + str(self.getQtd()) + " \n\n")


class Item:

    def __init__(self):
        self.carta = None
        self.qtd = None

    def getCarta(self):
        return self.carta

    def setCarta(self, carta):
        self.carta = carta

    def getQtd(self):
        return self.qtd

    def setQtd(self, qtd):
        self.qtd = qtd

    def decaiQtd(self):
        self.qtd -= 1

    def toString(self):
        return str(str(self.getCarta().toString()) + " Quantidade: " + str(self.getQtd())+"\n")


class Frete:
    def __init__(self):
        self.loja = None
        self.frete = None

    def getLoja(self):
        return self.loja

    def setLoja(self, loja):
        self.loja = loja

    def getFrete(self):
        return self.frete

    def setFrete(self, frete):
        self.frete = frete

    def toString(self):
        return "Loja "+str(self.getLoja())+": "+str(self.getFrete())+"\n"


class Fretes:
    def __init__(self):
        self.fretes = []

    def getFrete(self, id):
        return self.fretes[id]

    def geraVetorFrete(self, vetFrete):
        vetFrete[1].pop(0)
        for i in vetFrete[1]:
            frete = Frete()
            frete.setLoja(vetFrete[1].index(i))
            frete.setFrete(vetFrete[1][vetFrete[1].index(i)])
            self.fretes.append(frete)

    def toString(self):
        texto = ""
        for frete in self.fretes:
            texto += str(frete.toString())
        return texto


class Pedido:
    def __init__(self):
        self.pedido = []

    def getPedido(self):
        return self.pedido

    def setPedido(self, pedido):
        self.pedido = pedido

    def toString(self):
        texto = ""
        for item in self.pedido:
            texto += item.toString()
        return texto

    def tamanhoPedido(self):
        return len(self.pedido)

    def geraPedido(self, vetPedido, vetPrecos, vetQtds):
        for id in vetPedido:
            nome = vetPrecos[int(id[0])].pop(0)
            vetQtds[int(id[0])].pop(0)
            carta = Carta()
            carta.setId(int(id[0]))
            carta.setNome(nome)
            carta.setPrecos(vetPrecos[int(id[0])])
            carta.setQtd(vetQtds[int(id[0])])
            pedidoStatus = Item()
            pedidoStatus.setCarta(carta)
            pedidoStatus.setQtd(id[1])
            self.pedido.append(pedidoStatus)


class Gene:
    def __init__(self):
        self.carta = None
        self.loja = None

    def getCarta(self):
        return self.carta

    def setCarta(self, carta):
        self.carta = carta

    def getLoja(self):
        return self.loja

    def setLoja(self, loja):
        self.loja = loja

    def toString(self):
        return "Carta: " + str(self.carta.getNome()) + "\nId Loja: " + str(self.loja) + "\n"


class Cromossomo:
    def __init__(self):
        self.cromossomo = []
        self.fitness = None

    def getCromossomo(self):
        return self.cromossomo

    def getFitness(self):
        return self.fitness

    def preencherCromossomo(self, pedido, frete):
        copiaPedido = copy.deepcopy(pedido)
        for item in copiaPedido.getPedido():
            vet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
                   44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]
            random.shuffle(vet)
            for j in range(int(item.getQtd())):
                for i in vet:
                    loja = item.getCarta().getQtd()[i]
                    try:
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
        fitness = 0
        vetLoja = []
        for gen in self.cromossomo:
            #print("Carta" +str(gen.getCarta().getNome())+"Preco Carta: " + str(float(gen.getCarta().getPrecos()[gen.getLoja()])))
            fitness += float(gen.getCarta().getPrecos()[gen.getLoja()])
            if gen.getLoja() not in vetLoja:
                #print("Preco Frete: " + str(float(frete.getFrete(gen.getLoja()).getFrete()))+ " Loja: " + str(gen.getLoja()))
                fitness += float(frete.getFrete(gen.getLoja()).getFrete())
                vetLoja.append(gen.getLoja())
        self.fitness = fitness


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


def lerArquivo(caminho):
    vet = []
    f = open(caminho, 'r')
    for line in f:
        c = []
        linha = line.split("	")
        for collun in linha:
            c.append(collun)
        vet.append(c)
    return vet


def lerArquivo2(caminho):
    vet = []
    f = open(caminho, 'r')
    for line in f:
        c = []
        linha = line.split("|")
        for collun in linha:
            c.append(collun)
        vet.append(c)
    return vet


def listaIdPedido(vetPedido):
    listaPedido = []
    for item in vetPedido:
        listaPedido.append([int(item[0]), int(item[1])])
    return listaPedido


def cartas(vetPedido, vetPrecos, vetQtds):
    vetCards = []
    for id in vetPedido:
        nome = vetPrecos[int(id[0])].pop(0)
        vetQtds[int(id[0])].pop(0)
        carta = Carta()
        carta.setId(int(id[0]))
        carta.setNome(nome)
        carta.setPrecos(vetPrecos[int(id[0])])
        carta.setQtd(vetQtds[int(id[0])])
        vetCards.append(carta)
    return vetCards


def toStringArrayCartas(vetCartas):
    texto = ""
    for carta in vetCartas:
        texto += str("Id Carta: " + str(carta.getId()) + "\nNome: " + str(carta.getNome()) +
                     "\nVetor de Precos: \n" + str(carta.getPrecos()) + " \nVetor de Quantidades: \n" + str(carta.getQtd()) + " \n\n")
    return texto


vetFretes = lerArquivo("arquivos/ligamagicFrete.txt")
pedido1 = lerArquivo("arquivos/ligamagicPedido1.txt")
pedido2 = lerArquivo("arquivos/ligamagicPedido2.txt")
pedido3 = lerArquivo("arquivos/ligamagicPedido3.txt")
pedido4 = lerArquivo("arquivos/ligamagicPedido4.txt")
vetPreco = lerArquivo2("arquivos/ligamagicPreco.txt")
vetQtd = lerArquivo2("arquivos/ligamagicQtd.txt")

pedido = Pedido()
pedido.geraPedido(pedido1, vetPreco, vetQtd)

frete = Fretes()
frete.geraVetorFrete(vetFretes)

populacao = Populacao(pedido, frete, 100)
print(populacao.toStringValor())
print(populacao.getTop1().getFitness())

'''
for i in range(10):
    cromossomo = Cromossomo()
    cromossomo.preencherCromossomo(pedido, frete)
    print(cromossomo.getFitness())
    # print(len(cromossomo.getCromossomo()))

for item in pedido.getPedido():
    print(str(item.getCarta().getNome())+ " - "+item.getQtd())
'''
