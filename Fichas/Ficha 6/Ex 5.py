def substitui(l,a,n):
    for i in range(len(l)):
        if l[i]==a:
            l[i]=n            
    return l

print ( substitui ([1, 2, 3, 2, 4], 2, 'a'))