def soma(a,b):
    print("O resultado é ",a+b)

#chamada com argumentos não nomeados
soma(5,6)
#chamada com argumentos nomeadados
soma(b=76,a=534)

#multiplicação com valores default
def mult(x,y,z=None):
    if z is not None:
        print(x*y*z)
    else:
        print(x*y)

mult(3,4,5)
mult(7,6)

#o valor que prevalecerá ao final será o global x
def f1():
    #print(x)
    global x
    x=10
    print(x)

    def f2():
        #global x
        x=15
        print(x)
    
    f2()


f1()

print(x)

x=200
def f():
    x=10
    print(x)

f()

#função ecom desempacotamento em python
def sominha (*args):
    total = 0
    for numeros in args:
        total+=numeros

    return total

numeros = 1,2,3,4,5,6,7,8,9,10,11,12
val = sominha(*numeros)
print("valor sominha",val,sep=" ")

