import frete


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


vetFretes = lerArquivo("arquivos/ligamagicFrete.txt")
fretes = frete.geraVetorFrete(vetFretes)
print(vetFretes)
print(frete.toString(fretes))
