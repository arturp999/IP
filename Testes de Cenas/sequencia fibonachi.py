def fib(n):
    n0=0
    n1=1
    for i in range(0,n):
        na = n0 + n1
        n0 = n1
        n1 = na
        print (na)

print (fib(5))