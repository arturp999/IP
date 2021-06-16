#h = 120/60 # km/h
#min = 60*60 # m/h

d = eval (input('insira a distancia (km) '))
t = eval (input('insira o tempo (minutos) '))

km_h = (60/t)*d
m_s = (60*t)/(d*1000)

print ('Velocidade media k/h e ', km_h)
print ('Velocidade media m/s e ', m_s)
