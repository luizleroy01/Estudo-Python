#example of exercise using set with objective to find second ocurrence of a number as a repetition

lista = [1, 2, 3, 4, 5,4,3,1,2,4,2,1]
no_repetition = set()
repetidos = set()

for e in lista:
    if e not in no_repetition:
        no_repetition.add(e)
    else:
        repetidos.add(e)

if len(no_repetition) > 0:
    print("Possui elementos repetidos")
    print(repetidos)
else:
    print("Nao possui elementos repetidos")