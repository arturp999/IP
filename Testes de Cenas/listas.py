
lista=[2,3,5,9,12,33,34,45]


def remove_multiplos(lst,n):
    res=[]
    for i in lst:
        if i % n ==0:
            res=res+[i]
        return res