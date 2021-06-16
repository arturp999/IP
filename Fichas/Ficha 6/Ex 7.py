
lista=['a', 2, 'b', 'a']

def posicoes_lista(lst,elemento):
    res=[]
    for i in range(len(lst)):
        if lst[i] == elemento:
            res.append(i)
    return res

print(posicoes_lista(lista,'a'))