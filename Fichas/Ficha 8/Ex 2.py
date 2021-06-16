


def existe_algarismo(n,a):
    for i in range(n):
        num = n%10
        if num == a:
            return True
        else:
            n=n//10
    return False

print (existe_algarismo(123234,2))

#Comparando usando strings
#def existe_algarismo(n,a):
    #if str(a) in str(n):
        #return True
    #else:
        #return False

#print (existe_algarismo(123234,2))
    
""" 
def remove_multiplos(l,n):
    for i in reversed(range(len(l))):
        if l[i] % n == 0:
            del(l[i])
    return l
print (remove_multiplos([2,3,5,9,12,33,34,45],3))
"""