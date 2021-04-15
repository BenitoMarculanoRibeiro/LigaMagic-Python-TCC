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


def listaIdPedido(vetPedido):
    listaPedido = []
    for item in vetPedido:
        listaPedido.append(int(item[0]))
    return listaPedido

def criarCard(id, nome, vetPrecos, vetQtds):
    vetPrecos.pop(0)
    vetQtds.pop(0)
    return id, nome, vetPrecos, vetQtds

def vetCards(vetPedido, vetPrecos, vetQtds):
    vetCards = []
    listaPedido = listaIdPedido(vetPedido)
    for id in listaPedido:
        nome = vetPrecos.pop(0)
        vetQtds.pop(0)
        c = id, nome, vetPrecos[id], vetQtds[id]
        vetCards.append(c)
    return vetCards


def criarCromossomo():
    return 0


# carregando arquivos
vetFrete = lerArquivo("arquivos/ligamagicFrete.txt")
vetPedido1 = lerArquivo("arquivos/ligamagicPedido1.txt")
vetPedido2 = lerArquivo("arquivos/ligamagicPedido2.txt")
vetPedido3 = lerArquivo("arquivos/ligamagicPedido3.txt")
vetPedido4 = lerArquivo("arquivos/ligamagicPedido4.txt")
vetPreco = lerArquivo("arquivos/ligamagicPreco.txt")
vetQtd = lerArquivo("arquivos/ligamagicQtd.txt")
vetCards1 = vetCards(vetPedido1, vetPreco, vetQtd)
vetCards2 = vetCards(vetPedido2, vetPreco, vetQtd)
vetCards3 = vetCards(vetPedido3, vetPreco, vetQtd)
vetCards4 = vetCards(vetPedido4, vetPreco, vetQtd)
for item in vetCards4:
    print(item)
