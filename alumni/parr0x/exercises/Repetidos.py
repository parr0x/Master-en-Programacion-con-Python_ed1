from collections import Counter
from random import randint
lista=[]
for va in range (0,10):
    lista.append(randint(0,5))
repetitions=[]
for count in Counter(lista).items():
    if count[1] > 1: repetitions.append(count[0])

print(lista)
print(repetitions)
