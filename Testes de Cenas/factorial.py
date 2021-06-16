"""factorial"""

n=int(input('Qual o numero?: '))

if n == 0:
    print(0)
if n == 1:
    print(1)
else:
    fat=1
    i=2
    while i <= n:
        fat = fat*i
        i = i + 1
        print(fat)

    

"""def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)"""
        
"""print (fatorial(5))"""