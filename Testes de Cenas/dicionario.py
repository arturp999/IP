
def agrupa_por_chave(pares):
    res = {}
    for par in pares:
        if par [0] not in res:
            res[par[0]] = []
        res[par[0]]=res[par[0]]+[par[1]]
    return res

print(agrupa_por_chave([('a',8),('b',9),('a',3)]))