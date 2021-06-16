def funcao_a(n):
    res=()
    i=1
    while i <= n:
        if n%i == 0:
            res=res+(i,)
        i=i+1
    return res

print(funcao_a(10))