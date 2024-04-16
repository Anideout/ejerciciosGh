#ciclos de repeticion

#for -> para
import os
import time
os.system ("cls")
cantidad = int(input("ingrese cantidad de notas\n"))
contadornota = 0
for x in range(cantidad):
    nota = float(input(f"ingrese nota {x+1} \n"))
    contadornota = contadornota + nota 
    print (f"de momento llevo sumado: {contadornota}")
promedio = contadornota / cantidad 
print(f"segun las {cantidad} notas, tu promedio es: {promedio}")                                        


