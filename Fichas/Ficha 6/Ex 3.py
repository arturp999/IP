l =[3,5,6,12,'A','B']


def duplica_elementos(l):
    d=[]
    for i in l:
        d=d+[i,i]
    return d

print(duplica_elementos(l))