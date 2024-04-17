# use of set structure with python

s1 = set() # empty set
s2 = {'Luiz',1,2,3} # set full of elements

# set data structure removes repetitions of elements

lista = [1,1,2,2,2,3,3,4,4,4]
print(lista)

set_lista = set(lista)

print(set_lista)

#methods of set data structure
set_lista.add(5)
set_lista.update(('Luiz',6,7,8))
print(set_lista)
set_lista.discard('Luiz')

print(set_lista)

#union

s3 = {8,9,10}

s4 = s3 | set_lista

print(s4)

s5 = s4 & s2

print(s5)

s6 = s4 - s2
print(s6)