
#num=str(input('Insere um numero: '))
#print('o numero invertido e' , num[::-1])

x=int(input('Insere um numero: '))
inverso=0

while x > 0:
    resto=x%10
    inverso=(inverso*10)+resto
    x=x//10

print(inverso)