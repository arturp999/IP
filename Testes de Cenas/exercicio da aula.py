"""Le um numero inteiro e devido o numero apresentado em um tuplo"""

def inteiro(n):
    if isinstance(n,int): #verifica se o argumento N e inteiro
        res=()
        while n!=0:
            res=(n%10,)+res
            n=n//10
        return res
    else:
        raise ValueError('Funcao:Argumento nao inteiro')
        
print(inteiro((34500)))