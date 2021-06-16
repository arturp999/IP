x=str(input('numero com zeros: '))

a=i=0
while i < len(x):
    if x[i]=="0" and x[i+1]=="0":
        a+=1
    i+=1
print('O numero tem ', a, ' zeros seguidos')
    
