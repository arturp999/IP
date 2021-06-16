def remove_multiplos(l,n):
    for i in reversed(range(len(l))):
        if l[i] % n == 0:
            del(l[i])
    return l
      
print (remove_multiplos([2,3,5,9,12,33,34,45],3))