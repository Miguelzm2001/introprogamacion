#---Quiz 2---#

#---Constantes---#
PreguntaOpcion = ''' Ingrese alguna de las siguientes opciones
    1.Convertir de Celsius a Farenheit o a Kelvin 
    2.Lista con clasificación de temperatura
    3.Mostrar temperaturas más altas y bajas, y cada cuánto se toma la temperatura
    4.Salir
'''

PreguntaTemperatura = '''
    C- Mostrar original en Celsius
    K- Mostrar en Kelvin
    F- Mostrar en Farenheit
'''

PreguntaTemperaturaPaciente = "Ingrese la temperatura del paciente :"

listaTemperaturaCorporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]


#---Conversion Temperatura---#
listaKelvin = []
for elemento in listaTemperaturaCorporal:
    conversor = round (elemento + 273.15)
    listaKelvin.append(conversor)

listaFarenheit = []
for elemento in listaTemperaturaCorporal:
    conversor = round ((elemento * 1.8)+32)
    listaFarenheit.append(conversor)



#---Entradas---#
print ("Bienvenido, estamos a su disposición")

OpcionEscogida = int (input(PreguntaOpcion))

while (OpcionEscogida !=4):
    #---Punto 1---#
    if (OpcionEscogida == 1):
        OpcionTemperatura = (input(PreguntaTemperatura))
        if (OpcionTemperatura == "C"):
            print("La conversion no es necesaria, su valor está en Celsius")
            print(listaTemperaturaCorporal)
        elif(OpcionTemperatura == "K"):
            print("Mostrando lista en grados Kelvin")
            print(listaTemperaturaCorporal)
        elif(OpcionTemperatura == "F"):
            print("Mostrando lista en grados Farenheit")
            print(listaTemperaturaCorporal)
        else:
            print("El valor ingresado no es valido")
    #---Punto 2---#
    elif (OpcionEscogida == 2):
        Temperatura = float(input(PreguntaTemperaturaPaciente))
        if (Temperatura < 36 ):
            print("Su temperatura es baja, puede tener hipotermia")
        elif (Temperatura >= 36 and Temperatura < 37.5):
            print("Su temperatura es normal, mantenga el cuidado")
        else:
            print("Su temperatura es alta, puede tener fiebre")
    #---Punto 3---#
    elif (OpcionEscogida == 3):
        print( "Esta es la temperatura mayor : " , max ( listaTemperaturaCorporal ))
        print("Esta es la temperatura menor : " , min ( listaTemperaturaCorporal ))
        print("La temperatura se toma cada : " , len ( listaTemperaturaCorporal ) / 24, "Horas")
    #------opcion4-----#
    else:
        print("Esta opcion es invalida")
    OpcionEscogida = int(input(PreguntaOpcion))

print("Gracias por contar con nosotros")
