# use of EOF with python
while True:
    try:
        entrada = str(input())
        entrada = entrada.split(" ")
        D = int(entrada[0])
        VF = int(entrada[1])
        VG = int(entrada[2])

        auxd1 = 12000 - D
        auxd2 = 12000 + D
        escapou = False

        while auxd1 > 0 and auxd2 > 0:
            auxd1 -= VF
            auxd2 -= VG

        if auxd1 <= 0:
            print('N')
        else:
            print('S')
    except EOFError:
        break
