def baralho ():
    resultado= []
    for Naipe in ['Ouros','Copas','Paus','Espadas']:
        for valores in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q','K']:
            resultado=resultado+[{Naipe:valores}]
    return resultado

print(baralho())
   
   
    
"""
Naipe=['Espadas','Copas','Ouros','Paus']
Vlr=['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] 
"""