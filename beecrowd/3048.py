
n = int(input())
linha = []
escolhido = 0
qt =0
for i in range(n):
    num = int(input())
    if num != escolhido:
        escolhido = num
        qt +=1

print(qt)
