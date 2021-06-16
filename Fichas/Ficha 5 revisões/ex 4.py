
def junta_ordenados(t1,t2):
    i=j=0
    res=()
    while i < len(t1) and j < len(t2):
        if t1[i] < t2[j]:
            res=res+(t1[i], )
            i=i+1
        else:
            res=res+(t2[j], )
            j=j+1
    res=res+t1[i:]+t2[j:]
    return res


print(junta_ordenados((0,2,34,200,210),(1,5,23)))


"""def junta_ordenados(t1,t2):  #usando o sorted
    juntos=sorted(t1+t2)
    for i in juntos:
        if i < 0 :
            return ('Erro so podes colocar numeros inteiros na lista')
    if i > 0:
        return (juntos)"""