n1=eval(input('Qual e o numero? '))
n2=eval(input('Qual e o segundo numero? '))

media= (n1+n2)/2


if media >= 9.50:
    print('Aprovado com media de: ', media)
elif media < 9.50:
    print('Reprovado com media de: ', media)