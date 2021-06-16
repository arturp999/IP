n = eval(input('Indique um numero de 1 a 15: ' ))

soma=0


while n < 1 or n > 15:
    n =eval(input('Numero de 1 a 15: '))


while n !=16:
    print(n,'+',soma,'=',n+soma)
    soma=soma+n
    n=n+1