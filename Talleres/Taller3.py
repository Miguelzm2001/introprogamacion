#--- Taller Condicionales---#
print ("#"*15, "Punto 1", "#"*15)
#---Punto 1---#
#---Constantes---#
MENSAJE_ENTRADA = "Hola, bienvenido al mundo mágico"
MENSAJE_NUMERO_MAYOR = "El numero A es mayor que B"
MENSAJE_NUMERO_MENOR = "El numero A es menor que B"
MENSAJE_NUMERO_IGUAL = "A y B son iguales"
numeroA = 10
numeroB = 7

#---Entrada de código---#
print (MENSAJE_ENTRADA)
isMayor = numeroA < numeroB
isMenor = numeroA > numeroB

if (isMayor) :
    print (MENSAJE_NUMERO_MAYOR)
elif  (isMenor) :
    print (MENSAJE_NUMERO_MENOR)
else : 
    print (MENSAJE_NUMERO_IGUAL)

#---Punto 2---#
#---Constantes---#
PREGUNTA_EDAD = "Cuántos años tienes? : "
MENSAJE_MENOR_EDAD = "Eres un niño, duerme bien"
MENSAJE_JOVEN = "Eres joven, disfruta de ello"
MENSAJE_ADULTO = "Eres adulto, respira y no te estreses "
MENSAJE_ADULTO_MAYOR = "Eres de la tercera edad, sigue respirando"

#---Entrada de código---##
Edad = int(input(PREGUNTA_EDAD))
isMenorEdad = Edad < 18
isJoven = Edad >= 18 and Edad < 25
isAdulto = Edad >= 26 and Edad < 60
isAdultoMayor = Edad >= 60


if(isMenorEdad):
    print (MENSAJE_MENOR_EDAD)
elif(isJoven):
    print ( MENSAJE_JOVEN)
elif(isAdulto):
    print (MENSAJE_ADULTO)
else:
    print (MENSAJE_ADULTO_MAYOR)


#---Punto 3---#
#---Constantes---#
PREGUNTA_AÑO =  "Digita año en el que estás actualmente :"
PREGUNTA_ÚLTIMO_MUNDIAL_DISPUTADO = "Digita el año del último mundial jugado :"
PREGUNTA_PRÓXIMO_MUNDIAL_A_DISPUTAR = "Digita el año del próximo mundial a jugar :"
MENSAJE_TIEMPO_FALTANTE = "Relajate, faltan"
MENSAJE_TIEMPO_DESDE_UILTIMO = "Han pasado"

#---Entrada de código---#
Año_actual = int (input (PREGUNTA_AÑO))
MundialPasado = int ( input (PREGUNTA_ÚLTIMO_MUNDIAL_DISPUTADO))
PróximoMundial = int ( input (PREGUNTA_PRÓXIMO_MUNDIAL_A_DISPUTAR))
isAñosdesdeultimomundial = Año_actual - MundialPasado
isAñodelproximomundial = Año_actual + PróximoMundial


if(isAñosdesdeultimomundial) :
    print ( MENSAJE_TIEMPO_DESDE_UILTIMO, Año_actual - MundialPasado, "año/s")

if(isAñodelproximomundial) :
    print( MENSAJE_TIEMPO_FALTANTE, PróximoMundial - Año_actual, "año/s")


print ("#"*15, "Punto 4", "#"*15)
#---Punto 4---#
#---Constantes---#
PREGUNTA_DISTANCIA = "Digita una distancia en centímetros : "
MENSAJE_KILOMETROS = "Digita una distancia en kilómetros"
MENSAJE_METROS = "Digita una distancia en metros"
MENSAJE_CENTIMETROS = "Digita una distancia en centimetros"

#---Entrada código---#
Distancia = float (input(PREGUNTA_DISTANCIA))
isKilometros = Distancia * 10**-5
isMetros = Distancia * 10**-2

if(isKilometros):
    print(Distancia * 10**-5,MENSAJE_KILOMETROS)

if(isMetros):
    print(Distancia * 10**-2, MENSAJE_METROS )









