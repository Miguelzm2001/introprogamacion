pruebaV = True
pruebaF = False
print (pruebaV)
print (pruebaF)
pruebaV = pruebaF
print (pruebaV)
edad = 27
estatura = 1.67
peso = 84
NOMBRE = "Miguel Zuleta"
print ("#"*15, "Mayor Edad", "#"*15 )
ismayorEdad = edad >= 18
print (ismayorEdad)
print ("#"*15, "Bajo la Estatura promedio", "#"*15)
isMayorEstatura = estatura < 1.70 
print (isMayorEstatura) 
print ("#"*15, "Peso diferente 84", "#"*15)
isPesoDiferente = peso != 84
print (isPesoDiferente)
apellido = "Zuleta"
isApellido = apellido in NOMBRE
print ("#"*15, "Esta apellido en el nombre?", "#"*15)
print (isApellido)



