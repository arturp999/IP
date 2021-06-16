n1 = eval(input('insira um numero: '))
n2 = eval(input('insira outro numero: '))
n3 = eval(input('insira um terceiro numero: '))

if n1 > n2 and n1 > n3 :
    print('numero maior', n1)

if n3 > n2 and n3 > n1 :
    print('numero maior', n3)

if n2 > n3 and n2 > n1 :
    print('numero maior', n2)