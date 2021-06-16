
def triangular(t):
  num=0
  for i in range(1,t):
    num=num+i
    if t == num:
      return True
    if t == 1:
      return True    
  else:
    return False
    
print(triangular(8))

"""formula dos numeros triangulares
number = 0
number = number + i
"""