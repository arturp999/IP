print("Insira numeros inferiores a 100")
total= 0
cont = 0

while total<500:
    num= int(input("Numero: "))
    if num<100:
        total=total+num
        print("Total ate ao momento: ", total)
        cont=cont+1
        
    else:
        print("Numero nao aceite")

media=total/cont        
print("A media da soma e : ", round(media,0))