numero_1 = 0
numero_2 = 1


for i in range(1, 10):  
  prox_termo = numero_1 + numero_2 
  print(prox_termo)      
  numero_1 = numero_2                
  numero_2 = prox_termo
  