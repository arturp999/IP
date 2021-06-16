def numero(n):
    n= int(input('Numero? de 1 a 20: '))
    if n < 1:
        return 'Numero Invalido'
    if n >= 21:
        return 'Numero Invalido'
    else:
        return 'O numero que indicou e',n
    
    
print(numero(1))