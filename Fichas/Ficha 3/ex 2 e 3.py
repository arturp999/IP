#ex2
def area_circulo (r1):
    area=3.14*(r1*r1)
    return area

#ex3
def area_coroa (r1,r2):
    if r1<r2:
        raise ValueError
    else:
        area_coroa= area_circulo (areaext) - area_circulo (areaint)
        return area_coroa

areaext= eval (input ('insira raio exterior: '))
areaint = eval (input ('insira raio interior: '))
print(area_coroa(areaext,areaint))