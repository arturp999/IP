
def junto(x):
    i=e1=0
    for e in x:
        if e==e1:
            i+=1
        e1=e
    return i

print(junto((1,2,2,3,4,4)))
 
