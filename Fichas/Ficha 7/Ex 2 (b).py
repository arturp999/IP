container = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

def baralhar_cartas(dicionario,cartas):
    devolver=dicionario
    cont = 0
    while cont <= 4:
        devolver[0] [cont] = random.sample(cartas,len(cartas))
        cont = cont + 1
    return devolver

print (baralhar_cartas(dicionario,container))