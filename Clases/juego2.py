import random
#---Entradas---#
MENSAJE_SALUDO = "Bienvenido, que comience el juego" 
PREGUNTA_NUMERO = '''
        En este juego debes asetar un número entero
        que va desde el 1-10, la idea es que 
        lo puedes intentar las veces que 
        quieras...
        Muchos éxitos, ingresa tu numero
'''
PREGUNTA_DIFICULTAD ='''
    1- Fácil
    2- Moderado
    3- Difícil
'''

PREGUNTAR_FALLIDA = 'Aaaaah! Fallaste ☻☺☻♥♦♣♠• ingresa otro número :'
MENSAJE_GANASTE = 'Felicidades ganaste!!'
MENSAJE_PERDISTE = 'Perdiste D: "vuelve" a intentarlo!!'

#---Entada al código---#
numeroOculto = random.randint (1,10)
vidas = None

dificultad =int (input(PREGUNTA_DIFICULTAD))
while (dificultad !=1 and dificultad !=2 and dificultad !=3) :
    print ("Ingresa una opción válida")
    dificultad = int (input(PREGUNTA_DIFICULTAD))

if (dificultad == 1):
    print ("Modo fácil activado")
    vidas = 5
elif (dificultad == 2):
    print ("Modo medio activado")
    vidas = 3
else :
    ("Modo difícil activado")
    vidas = 1


numeroIngresado = int (input(PREGUNTA_NUMERO))
while(numeroIngresado != numeroOculto and vidas>1) :
    vidas -=1
    print (f'te quedan {vidas} vidas')
    numeroIngresado = int(input(PREGUNTAR_FALLIDA))

if (vidas >=0 and numeroIngresado == numeroOculto):
    print(MENSAJE_GANASTE)
else :
    print (MENSAJE_PERDISTE, "El numero oculto era el", numeroOculto )
