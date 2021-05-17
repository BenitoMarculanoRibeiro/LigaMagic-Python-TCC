# coding: utf-8
from .Item import Item
from .Carta import Carta
from .Frete import Frete
from json import load


def lerArquivo(caminho):
    vet = []
    for line in open(caminho, 'r'):
        c = []
        linha = line.split("	")
        for collun in linha:
            c.append(collun.rstrip("\n"))
        vet.append(c)
    return vet


def lerArquivo2(caminho):
    vet = []
    for line in open(caminho, 'r'):
        c = []
        linha = line.split("|")
        for collun in linha:
            collun = collun.rstrip("\n")
            c.append(collun)
        vet.append(c)
    return vet


def toStringPedido(pedido):
    texto = ""
    for item in pedido:
        texto += item.toString()
    return texto


def tamanhoPedido(pedido):
    return len(pedido)


def geraPedido(vetPedido, vetPrecos, vetQtds):
    pedido = []
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
        pedido.append(pedidoStatus)
    return pedido


def geraVetorFrete(vetFrete):
    vetFrete[1].pop(0)
    fretes = []
    for i in vetFrete[1]:
        frete = Frete()
        frete.setLoja(vetFrete[1].index(i))
        frete.setFrete(vetFrete[1][vetFrete[1].index(i)])
        fretes.append(frete)
    return fretes


def toStringFrete(fretes):
    texto = ""
    for i in fretes:
        texto += "Loja " + str(i.getLoja()) + " - " + str(i.getFrete()) + "\n"
    return texto


def escrever_json(caminho, lista):
    arquivo = open(caminho, 'a')
    arquivo.write(lista)


def carregar_json(arquivo):
    with open('pedido1.json', 'r') as f:
        return load(f)


def converter(pedido, arrayInicioPopulacao, arraySelecao, arrayCruzamtento, arrayMutacao, arrayInsercao, arrayTempoTotal, arrayFitness):
    texto = "{\n    \""+str(pedido)+"\":[{\n"

    for i in range(len(arrayTempoTotal)):
        if(i == 0):
            texto += "\"" + str(arrayTempoTotal[i]) + "\": ["
        elif(i == len(arrayTempoTotal)-1):
            texto += "\"" + str(arrayTempoTotal[i]) + "\"]"
        else:
            texto += "\"" + str(arrayTempoTotal[i]) + "\" , "

    texto += "},\n{"
    for i in range(len(arrayFitness)):
        if(i == 0):
            texto += "\"" + str(arrayFitness[i]) + "\": ["
        elif(i == len(arrayFitness)-1):
            texto += "\"" + str(arrayFitness[i]) + "\"]"
        else:
            texto += "\"" + str(arrayFitness[i]) + "\" , "

    texto += "},\n    {"

    for i in range(len(arrayInicioPopulacao)):
        if(i == 0):
            texto += "\"" + str(arrayInicioPopulacao[i]) + "\": ["
        elif(i == len(arrayInicioPopulacao)-1):
            texto += "\"" + str(arrayInicioPopulacao[i]) + "\"]"
        else:
            texto += "\"" + str(arrayInicioPopulacao[i]) + "\" , "

    texto += "},\n{"
    for i in range(len(arraySelecao)):
        if(i == 0):
            texto += "\"" + str(arraySelecao[i]) + "\": ["
        elif(i == len(arraySelecao)-1):
            texto += "\"" + str(arraySelecao[i]) + "\"]"
        else:
            texto += "\"" + str(arraySelecao[i]) + "\" , "

    texto += "},\n    {"

    for i in range(len(arrayCruzamtento)):

        if(i == 0):
            texto += "\"" + str(arrayCruzamtento[i]) + "\": ["
        elif(i == len(arrayCruzamtento)-1):
            texto += "\"" + str(arrayCruzamtento[i]) + "\"]"
        else:
            texto += "\"" + str(arrayCruzamtento[i]) + "\" , "

    texto += "},\n{"
    for i in range(len(arrayMutacao)):
        if(i == 0):
            texto += "\"" + str(arrayMutacao[i]) + "\": ["
        elif(i == len(arrayMutacao)-1):
            texto += "\"" + str(arrayMutacao[i]) + "\"]"
        else:
            texto += "\"" + str(arrayMutacao[i]) + "\" , "

    texto += "},\n    {"

    for i in range(len(arrayInsercao)):

        if(i == 0):
            texto += "\"" + str(arrayInsercao[i]) + "\": ["
        elif(i == len(arrayInsercao)-1):
            texto += "\"" + str(arrayInsercao[i]) + "\"]"
        else:
            texto += "\"" + str(arrayInsercao[i]) + "\" , "

    texto += "}]\n}"
    return texto
