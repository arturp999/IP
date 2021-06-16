euros=eval(input('Valor em Euros? Se for em libras introduz 0: '))

libras=1.16
if euros < 1:
    euros=eval(input('Valor em Libras? '))
    valor=round(libras*euros,3)
    diferenca=round(valor-euros,3)
    print('O valor de libras em euros: ', valor, 'O valor de diferenca que ganhamos', diferenca, 'euros')

elif euros > 1:
    libras=1.16
    x=euros//libras
    y=euros%libras
    h=round(x+y,3)
    diferenca=round(euros-h,3)
    print('O valor em libras e de: ',h, 'o valor que perdemos: ',diferenca)
