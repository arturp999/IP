def soma_quadrados(n):
    total=0
    for i in range(1,n+1):
        quadrado1=i*i
        total=quadrado1+total
    return 'A soma de todos os quadrados ate ao numero indicado e de:',total
        
print(soma_quadrados(3))

"""n = int(input("Queres o quadrado ate que numero? "))º
for i in range(1,n+1):
    total=0
    quadrado1=i*i
    total=quadrado1+total
    print('A soma dos quadrados de todos os numeros ate',n,'e de:',total)
    """