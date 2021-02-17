#---Preguntas y Mensajes---#
PREGUNTA_numeroZ = "cual es el numero Z?  :  "
PREGUNTA_numeroX = "cual es el numero X?  :  "
MENSAJE_SUMA = "el resultado de la suma Z + X  es :"
MENSAJE_RESTA = "el resultado de la resta de Z - X es :"
MENSAJE_MULTIPLICACION = "el resultado de la multiplicacion de Z*X es :"
MENSAJE_EXPONENTE = "el exponente de Z**X es :"
MENSAJE_DIVISION = "el resultado de la division de Z/X es :"

#---Código Número entero---#
numeroZ = int(input(PREGUNTA_numeroZ))
numeroX = int(input(PREGUNTA_numeroX))
isMayorZ = numeroZ >= numeroX
print ("la ecuacion de Z >= a X es", isMayorZ)
print (MENSAJE_SUMA, numeroZ + numeroX)
print (MENSAJE_RESTA, numeroZ - numeroX)
print (MENSAJE_MULTIPLICACION, numeroZ * numeroX)
print (MENSAJE_EXPONENTE, numeroZ ** numeroX)
print (MENSAJE_DIVISION, numeroZ / numeroX)


#---Código Número decimal---#
numeroA = float(input(PREGUNTA_numeroZ))
numeroB = float(input(PREGUNTA_numeroX))
isMayorZ = numeroZ >= numeroX
print ("la ecuacion de Z >= a X es", isMayorZ)
print (MENSAJE_SUMA, numeroZ + numeroX)
print (MENSAJE_RESTA, numeroZ - numeroX)
print (MENSAJE_MULTIPLICACION, numeroZ * numeroX)
print (MENSAJE_EXPONENTE, numeroZ ** numeroX)
print (MENSAJE_DIVISION, numeroZ / numeroX)