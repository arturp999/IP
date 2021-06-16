def soma_quadrado_while(n):
    i=0
    resultado = 0
    while i != len(n):
        resultado = resultado + n[i]*n[i]
        i=i+1
    return resultado

print (soma_quadrado_while([1,2,3]))


#def soma_quadrado_for(lst):
            #resultado = 0
            #for i in range(0,len(lst)):
                        #resultado = resultado + lst[i]*lst[i]
            #return resultado
            
#print (soma_quadrado_for([1,2,3]))