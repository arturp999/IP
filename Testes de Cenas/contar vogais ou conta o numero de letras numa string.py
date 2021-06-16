#contar as vogais

def contar(f):
    vogais=("a","e","i","o","u")
    j=0
    for i in range(0,len(f)):
        if f[i] in vogais:
            j+=1
    return print('A frase tem',j,'vogais')

print (contar("uma vezuma vezuma vezuma vezuma vez"))