prod=eval(input('Quantidade do produto? '))
val=eval(input('Preco por unidade? '))

conta=val*prod
if prod < 500:
    conta=prod*val
    print('Valor a pagar sem desconto: ',conta)

elif prod >=1000:
    desconto=(val*prod)*0.08
    conta=(val*prod)-desconto
    print('Valor a pagar ja com o desconto de 8% e:',conta, 'o valor de desconto e:', desconto,'euros')

else:
    desconto=(val*prod)*0.05
    conta=(val*prod)-desconto
    print('Valor a pagar ja com o desconto de 5% e:',conta, 'o valor de desconto e:', desconto,'euros')
