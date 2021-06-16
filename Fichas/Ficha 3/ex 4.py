"""formula para o troco"""
def troco(valor):
    lista=(5000,2000,1000,500,200,100,50,20,10,5,2,1)
    centimos=int((valor*1000/10))
    for c in lista:
        if (c >= 500):
            if (centimos // c > 0):
                print('Nota de', c/100,'euros =',centimos//c)
        elif (c < 500 and c > 50):
            if(centimos//c != 0):
                print('Moeda de', c/100,'euros =',centimos//c)
        else:
            if(centimos//c != 0):
                print('Moeda de',c,'centimos =',centimos//c)
        centimos=centimos%c
        
print(troco(1852.21))
"""dizer foi mais que 1 nota indicar notas"""