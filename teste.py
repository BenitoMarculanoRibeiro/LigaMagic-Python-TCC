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
vetQtd = lerArquivo2("arq/ligamagicQtd.txt")
cont =0

print(len(vetQtd[-1]))
print(len(vetQtd[11129]))
for item in vetQtd[11139]:
    if(item!= vetQtd[11139][0]):
        #print(str(item)+ "snbd")
        cont=int(item)+ cont
print(cont)

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
vetFretes[1].pop(0)
print(vetFretes[1])
print(len(vetFretes[1]))
