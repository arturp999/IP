b = [
{'Titulo' : 'Matematica para Engenheiros', 'ano' : 1990},
{'Titulo' : 'Matematica para Engenheiros', 'ano' : 2007},
{'Titulo' : 'Contas para burros', 'ano' : 2008},
{'Titulo' : 'Aprender a Programar','ano' : 2009},
{'Titulo' : 'Nao sei o que tou fazendo','ano' : 2010},
{'Titulo' : 'Ajuda','ano' : 2011},
]

def mais_antigo(b):
    data_mais_antigo=b[0]['ano']
    titulo_mais_antigo=b[0]['Titulo']
    for i in range(1,len(b)):
        if b[i]['ano'] < data_mais_antigo:
            data_mais_antigo=b[i]['ano']
            titulo_mais_antigo=b[i]['titulo']
    print('data mais antigo: ',data_mais_antigo)
    print('titulo mais antigo: ',titulo_mais_antigo)
    return 

print (mais_antigo(b))