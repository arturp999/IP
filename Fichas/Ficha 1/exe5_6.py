#dias = eval (input('Numero de dias'))

segundos = eval (input('Numero segundos '))
dias = segundos//86400
restosegundos = segundos%86400
horas = restosegundos // 3600
minutos = restosegundos//60
segundos = restosegundos%60

print ('dias:',dias,'horas: ',horas, 'minutos: ', minutos, 'segundos: ', segundos)
