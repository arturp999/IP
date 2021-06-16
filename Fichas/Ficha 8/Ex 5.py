def soma_quadrados_valores(d):
    resultado = 0
    for i in d:
        resultado = resultado + d[i]*d[i]
    return resultado

print (soma_quadrados_valores({'a':2,'3':5,'c':3}))