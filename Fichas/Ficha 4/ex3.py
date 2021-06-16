pares=(2,5,6,7,9,1,8,8)

def par(t):
    pares=()
    for cont in t:
        if cont % 2 == 0:
            pares=pares+(cont,)
    return pares

print(par(pares))
