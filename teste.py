import random

vetor = [["Banana", 5], ["Abroba", 1], ["Cleiton", 3],
         ["Marcos", 2], ["Marquin", 4], ["Leite", 0]]


def mergeSort(alist):
    #print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][1] < righthalf[j][1]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
    #print("Merging ", alist)


def roleta(lista):
    vetor = []
    cont = len(lista)
    for i in lista:
        for j in range(cont):
            vetor.append(i)
        cont -= 1
    print(vetor)
    random.shuffle(vetor)
    print(vetor)
    result = lista.pop(0)
    return result


print(vetor)
mergeSort(vetor)
print(vetor)
print(roleta(vetor))
