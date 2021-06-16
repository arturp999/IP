
def num_divisores(d):
    divisores=0
    for i in range(1,d+1):
        if d % i == 0:
            divisores=divisores+1
    return divisores

print(num_divisores(20))

"""d= int(input("Quantos divisores tem o numero?:  "))
divisores=0
for i in range(1,d+1):
    if d % i == 0:
        divisores=divisores+1
print (divisores)"""