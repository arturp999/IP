
def cria_lista_multiplos(m):
    res=[]
    for i in range(10):
        res = res+[m*i]
        #res.append(mult)
    return res  

print (cria_lista_multiplos(6))