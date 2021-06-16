# 7.5

d = {'a' :[1,2],'b':[1,5],'c':[9], 'd':[4]}

def inverte_dic(d):
    resultado={}
    for i in d:
        for v in d [i]:
            if v in resultado:
                print  (i)
                print (v)                
                resultado[v]+=[i]
            else:
                resultado[v]=[i]
    return resultado

print (inverte_dic(d))



