import math
# use of EOF with python
while True:
    try:
        entrada = str(input())
        entrada = entrada.split(" ")
        D = int(entrada[0])
        VF = int(entrada[1])
        VG = int(entrada[2])

        #calculo da trajetória da guarda costeira como se fosse uma hipotenusa
        dist = math.sqrt(144 + D * D)
        pf = 12/VF
        pg = dist/VG
        if pg <= pf:
            print('S')
        else:
            print('N')
    except EOFError:
        break
