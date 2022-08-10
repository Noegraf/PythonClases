'''Escribe un programa en la consola de python que pida al usuario
su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y
lo almacene en una variable,
e imprima por pantalla la frase
Tu índice de masa corporal es
donde 
es el índice de masa corporal calculado
redondeado con dos decimales. '''

import math


peso = int(input("Ingresa tu peso en Kg: "))
altura = int(input("Ingresa tu altura en Mt: "))

ind_masa_corporal = peso / math.sqrt(altura)
ind_masa_redondeado = round(ind_masa_corporal, 2)

print ("Tu índice de masa corporal es "+str(ind_masa_corporal)+" donde "+str(ind_masa_redondeado)+" es el índice de masa corporal calculado redondeado con dos decimales")



