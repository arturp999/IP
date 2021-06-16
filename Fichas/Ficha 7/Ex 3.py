def conta_palavras(frase):
    resultado={}
    palavras=frase.split()
    for palavra in palavras:
        if palavra not in resultado:
            resultado[palavra]=1
        else:
            resultado[palavra]=resultado[palavra]+1
    return resultado

frase="um dois tres um welcome to the jujngles wlecome welcome"
print(conta_palavras(frase))

"""
def contar_palavras(string):
    string = string.split()
    dicionario = {}
    for i in string:
        dicionario[i] = i.count(i)
    print ('Foram introduzidas', len(dicionario), 'Palavras!')
    return dicionario

print(contar_palavras('a  asdasd  asdasa a'))
"""
