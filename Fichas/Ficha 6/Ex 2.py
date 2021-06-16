
def junta_ordenados(l1,l2):
    i=0
    j=0
    res=[]
    while i <len(l1) and j < len(l2):
        if l1[i] < l2 [j]:
            res.append(l1[i])
            i=i+1
        else:
            res.append(l2[j])
            j=j+1
    res=res+l1[i:]+l2[j:]
    return res

print (junta_ordenados([2,5,90],[3,5,6,12]))


"""
l1 =[2,5,90]
l2 =[3,5,6,12]
l3=sorted(l1+l2)
print(l3)"""