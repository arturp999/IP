num = str (input('coloca um numero: '))

i=a=0
b=" "

while i < len(num):
    a=int(num[i])
    if a %2 !=0:
        b=b+num[i]
    i+=1

print('Impares: ', b)