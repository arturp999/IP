#FAZER COM UM WHILE

x=int(input('Insere um numero 1 e 5:  '))

while x < 1 or x > 5:
     print('Nao aceite')
     x=int(input('Insere um numero 1 e 5:  '))
else:
     print('o numero' , x)