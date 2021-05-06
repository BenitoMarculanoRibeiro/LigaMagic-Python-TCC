from random import randint

def inverter(i):
    return 1 if i==0 else 0

i = randint(0, 1)
print(i)
i = inverter(i)
print(i)