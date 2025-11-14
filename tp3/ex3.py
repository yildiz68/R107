from random import *


nombre = int(input("tente une valeur "))
deviner = randint(0,100)
while nombre !=deviner:
    if nombre < deviner:
        nombre =int(input("essayer plus grand"))
    elif nombre > deviner:

        nombre= int(input("essayer plus petit"))
print("c'est ça")