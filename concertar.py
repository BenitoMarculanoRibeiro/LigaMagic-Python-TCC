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
        c = ""
        linha = line.split("	")
        for collun in linha:
            # print(c)
            if(collun == ''):
                n = randrange(0, 10)
                c += (str(n) + "|")
                #print("Alterado: " + str(n))
                # print(c)
            else:
                c += collun + "|"
        t.append(c)
    arquivo = open("arq/ligamagicQtd.txt", 'w')
    arquivo.writelines(t)
    arquivo.close()


def concertaArquivoPreco():
    arquivo = open("arquivo/ligamagicPreco.txt", 'r')
    conteudo = arquivo.readlines()
    t = []
    for line in conteudo:
        c = ""
        linha = line.split("	")
        for collun in linha:
            # print(c)
            if(collun == ''):
                n = round(uniform(0.05, 100), 2)
                c += (str(n) + "|")
                #print("Alterado: " + str(n))
                # print(c)
            else:
                c += collun + "|"
        t.append(c)

    arquivo = open("arq/ligamagicPreco.txt", 'w')
    arquivo.writelines(t)
    arquivo.close()


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
