'''
Tenho 2 listas com objetos.
Preciso cruzar as listas de forma aleatória.
Até aqui consigo fazer, mas não posso cruzar as lista separando objetos com mesmo Id.
Por exemplo: 
Se o ponto de corte aleatório cair na posição 4, tenho que cruzar de forma em que os objetos de Id 2 fiquem juntos, tendo que mudar o ponto de corte para entre os Ids 1 e 2 ou 2 e 3.
Tenho o seguinte código:
'''
import random


lista1 = [[0, "ba"], [1, "ca"], [1, "vi"], [2, "ka"],
          [2, "ra"], [2, "ne"], [3, "tan"], [3, "fa"]]
lista2 = [[0, "da"], [1, "py"], [1, "ti"], [2, "ta"],
          [2, "be"], [2, "ci"], [3, "cro"], [3, "to"]]

print(lista1)
print(lista2)

corte = random.randint(1, len(lista1))
print(corte)

filho1 = lista1[0:corte] + lista2[corte::]
filho2 = lista2[0:corte] + lista1[corte::]

print(filho1)
print(filho2)


#exclusão de elementos num intervalo


del(lista1[1:4])
print(lista1)

#exclusão de elementos que estejam entre intervalo
del(lista2[2::])
print(lista2)