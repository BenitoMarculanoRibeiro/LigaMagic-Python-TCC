from time import time
vet = []
vet.append(10)
vet.append(100)
vet.append(1000)
vet.append(10000)
vet.append(100000)
vet.append(1000000)
vet.append(10000000)
vet.append(100000000)
for k in vet:
    t1 = time()
    for j in range(10):
        i = 0
        for i in range(k):
            i += 1
    t2 = time()
    total = t2-t1
    print("Tamanho: " + str(k) + " Media Milisegundos: " + str(total/10))
