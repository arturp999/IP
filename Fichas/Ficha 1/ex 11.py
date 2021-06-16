horas = eval(input('Numero de horas? '))
sh = eval(input('Valor por hora? '))

if horas < 40:
    vh40= sh*horas
    print(vh40)
if  horas > 40:
    horas_normais=40*sh
    hs=horas-40
    valor_extra=(hs*sh)*2
    
    print('Valor total a receber ja com horas extra',horas_normais+valor_extra)