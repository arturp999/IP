
num1 = eval(input('Primeiro numero ? '))
op = str(input('+ - / * ? '))
num2 = eval(input('Segundo numero? '))   


while op == '+' or '-' or '/' or '*':
    if op == '+' :
        print('A soma de ambos os numeros e:', num1+num2)
        break
    elif op == '/':
        print('A divisao do numero e:', num1/num2)
        break
    elif op == '-':
        print('A subtracao do numero e:', num1-num2)
        break
    elif op == '*':
        print('A multiplicao do numero e:', num1*num2)
        break
    else:
        op = str(input('Tens de introduzir a operacao: + - / * ? '))
    


