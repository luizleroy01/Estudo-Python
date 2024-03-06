#A tuple is an object that seems  abit with lists but is a imutable objetc

tupla = (1,2,3,4,5)

for i in range(len(tupla)):
    if i % 2 == 0:
        print(tupla[i])