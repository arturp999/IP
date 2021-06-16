
def conta_menores(t,n):
    menores=0
    for i in t:
        if i < n:
            menores=menores+1
    return menores

print(conta_menores((3,4,5,6,7),(1)))


"""t=(3,4,5,6,7)
n=int(input('Inferior a que numero? '))
menores=0
for i in t:
    if i < n:
        menores=menores+1
print(menores)
""" 
#Isto e um input para pedir a user um tuplo
#t= tuple([int(x) for x in input("Indica os numeros com , : ").split(',')])