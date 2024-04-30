#exercise to interpretate roman algarisms
letters = {'I':1,'V':5,'X':10,'L':50,'C':100,'M':1000}
values = {'IV':4,'IX':9,'XL':40,'XC':90,'CM':900}

print(letters['I'])
print(letters['V'])

entrada = 'IV'
numero = 0

for i in range(0,len(entrada),2):
    print(entrada[i])
        