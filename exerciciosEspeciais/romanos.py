# exercise to interpretate roman algarisms
letters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "M": 1000}
entrada = "MCMXLV"

numero = 0
last = ''
value = 0

for i in range(0,len(entrada)-1):
    if entrada[i] == 'I' or entrada[i] == 'X' or entrada[i] == 'C':
        value = letters.get(entrada[i])
        if entrada[i+1] == 'V' or entrada[i+1] == 'L' or entrada[i+1] == 'M' or entrada[i+1] == 'X':
            numero -= value
        else:
            numero += value
    else:
        value = letters.get(entrada[i])
        numero += value

tam = len(entrada)
value = letters.get(entrada[tam-1])
numero += value
print(numero)
