def lerArquivo(caminho):
    vet = []
    f = open(caminho, 'r')
    for line in f:
        c = []
        linha = line.split("|")
        for collun in linha:
            c.append(collun)
        vet.append(c)
    return vet
vetPreco = lerArquivo("arq/ligamagicPreco.txt")
print(vetPreco)