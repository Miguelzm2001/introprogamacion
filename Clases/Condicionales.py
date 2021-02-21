#---Constantes---#
MENSAJE_BIENVENIDA = "Hola un gusto verte"
MENSAJE_MAYOR = "El número A es mayor que B"
MENSAJE_MENOR = "El número A es menor que B"
MENSAJE_IGUAL = "A y B son iguales"
PREGUNTA_NUMERO_A = "Ingrese un número A :"
PREGUNTA_NUMERO_B = "Ingrese un número B :"

#---Entrada al código---#
print(MENSAJE_BIENVENIDA)
numeroA = int (input(PREGUNTA_NUMERO_A))
numeroB = int (input(PREGUNTA_NUMERO_B))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB

if (isMayor) :
    print(MENSAJE_MAYOR)
elif (isMenor) :
    print(MENSAJE_MENOR)
else : 
    print (MENSAJE_IGUAL)

print(resultado)