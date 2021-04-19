# coding: utf-8
from random import randrange, uniform
# Algoritmo usado para concertar os arquivos conrrompidos
# Problema:
# Os aquivos tem posições vazias o que seria o equivalente a posições nulas.
# Solução:
# Como isso esse problema não agrega em nada o projeto decidi substituir as posições vazias por numeros aleatorios.


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


def lerArquivoAlterado(caminho):
    vet = []
    f = open(caminho, 'r')
    for line in f:
        c = []
        linha = line.split("|")
        for collun in linha:
            c.append(collun)
        vet.append(c)
    return vet


def concertaArquivoQtd():
    arquivo = open("arquivo/ligamagicQtd.txt", 'r')
    conteudo = arquivo.readlines()
    t = []
    for line in conteudo:
        if(conteudo[0] == line):
            c = ""
            linha = line.split("	")
            for i in range(88):
                if(i < 87):
                    n = randrange(0, 100)
                    c += (str(linha[i]) + "|")
                else:
                    n = randrange(0, 100)
                    c += (str(linha[i]))
            t.append(c)
        else:
            c = ""
            linha = line.split("	")
            for i in range(88):
                if(linha[0] == linha[i]):
                    c += (str(linha[i]) + "|")
                elif(i < 87):
                    if(linha[i] == ''):
                        n = randrange(0, 100)
                        c += (str(n) + "|")
                    else:
                        c += (str(linha[i]) + "|")
                else:
                    n = randrange(0, 100)
                    c += (str(n)+"\n")
            t.append(c)
    arquivo = open("arq/ligamagicQtd.txt", 'w')
    arquivo.writelines(t)
    arquivo.close()


def concertaArquivoPreco():
    arquivo = open("arquivo/ligamagicPreco.txt", 'r')
    conteudo = arquivo.readlines()
    t = []
    for line in conteudo:
        if(conteudo[0] == line):
            c = ""
            linha = line.split("	")
            for i in range(88):
                if(i < 87):
                    n = round(uniform(0.05, 100), 2)
                    c += (str(linha[i]) + "|")
                else:
                    n = round(uniform(0.05, 100), 2)
                    c += (str(linha[i]))
            t.append(c)
        else:
            c = ""
            linha = line.split("	")
            for i in range(88):
                if(linha[0] == linha[i]):
                    c += (str(linha[i]) + "|")
                elif(i < 87):
                    if(linha[i] == ''):
                        n = round(uniform(0.05, 100), 2)
                        c += (str(n) + "|")
                    else:
                        c += (str(linha[i]) + "|")
                else:
                    n = round(uniform(0.05, 100), 2)
                    c += (str(n)+"\n")
            t.append(c)
    arquivo = open("arq/ligamagicPreco.txt", 'w')
    arquivo.writelines(t)
    arquivo.close()


'''
def concertaArquivoQtd():
    arquivo = open("arquivo/ligamagicQtd.txt", 'r')
    conteudo = arquivo.readlines()
    t = []
    for line in conteudo:
        c = ""
        linha = line.split("	")
        for collun in linha:
            # print(c)
            if(collun == ''):
                n = randrange(0, 100)
                if(linha[87] != collun):
                    c += (str(n) + "|")
                else:
                    c += (str(n))
                #print("Alterado: " + str(n))
                # print(c)
            else:
                if(linha[87] != collun):
                    c += (str(collun) + "|")
                else:
                    c += (str(collun))
        t.append(c)
    arquivo = open("arq/ligamagicQtd.txt", 'w')
    arquivo.writelines(t)
    arquivo.close()
'''

'''
def concertaArquivoPreco():
    arquivo = open("arquivo/ligamagicPreco.txt", 'r')
    conteudo = arquivo.readlines()
    t = []
    for line in conteudo:
        c = ""
        linha = line.split("	")
        for collun in linha:
            if(collun == ''):
                n = round(uniform(0.05, 100), 2)
                if(linha[-1] != collun):
                    c += (str(n) + "|")
                else:
                    c += (str(n))
            else:
                if(linha[-1] != collun):
                    c += (str(collun) + "|")
                else:
                    c += (str(collun))
        t.append(c)

    arquivo = open("arq/ligamagicPreco.txt", 'w')
    arquivo.writelines(t)
    arquivo.close()
'''


vetQtd = lerArquivo("arquivo/ligamagicQtd.txt")
nu = 0
for item in vetQtd:
    if(str(item[1]) != "Site1"):
        for i in item:
            if(item[0] != i):
                if(i == ''):
                    nu += 1
print(nu)

concertaArquivoQtd()

vetQtd = lerArquivoAlterado("arq/ligamagicQtd.txt")
nu = 0
for item in vetQtd:
    if(str(item[1]) != "Site1"):
        for i in item:
            if(item[0] != i):
                if(i == ''):
                    nu += 1
print(nu)

vetQtd = lerArquivo("arquivo/ligamagicPreco.txt")
nu = 0
for item in vetQtd:
    if(str(item[1]) != "Site1"):
        for i in item:
            if(item[0] != i):
                if(i == ''):
                    nu += 1
print(nu)

concertaArquivoPreco()

vetQtd = lerArquivoAlterado("arq/ligamagicPreco.txt")
nu = 0
for item in vetQtd:
    if(str(item[1]) != "Site1"):
        for i in item:
            if(item[0] != i):
                if(i == ''):
                    nu += 1
print(nu)
'''


vetFretes = lerArquivo("arquivo/ligamagicFrete.txt")
pedido1 = lerArquivo("arquivo/ligamagicPedido1.txt")
pedido2 = lerArquivo("arquivo/ligamagicPedido2.txt")
pedido3 = lerArquivo("arquivo/ligamagicPedido3.txt")
pedido4 = lerArquivo("arquivo/ligamagicPedido4.txt")
vetPreco = lerArquivo("arquivo/ligamagicPreco.txt")
vetQtd = lerArquivo("arquivo/ligamagicQtd.txt")

for item in vetQtd:
    if(str(item[1]) != "Site1"):
        for i in item:
            if(item[0]!=i):
                if(i==''):
                    i = random.randrange(0, 100)


numero = round(3.32424, 2)
print(numero) // 3.32
'''
