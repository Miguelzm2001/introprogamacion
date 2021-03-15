#---Taller 4---#


preguntaNumero = '''Ingrese alguna de estas opciones
    1.Hacer conversión de Dolares a COP o Euros
    2.Mostrar lista con clasificación de ingresos
    3.Mostrar valor más alto, más bajo y promedio
    4.Salir
'''
preguntaMoneda = '''
    D- Mostrar original en Dolares
    C- Mostrar en COP
    E- Mostrar en Euros
'''

preguntaIngresos = "De cuánto es su ingreso económico mensual en Dolares?"

listaDolares = [20000,30000,4000,2500,1000,7600]

#---Conversion punto 1---#
listaPesos = []
for elemento in listaDolares:
    conversor = round (elemento * 3700)
    listaPesos.append(conversor)

listaEuros = []
for elemento in listaDolares:
    conversor = round (elemento*0.00023)
    listaEuros.append(conversor)



#---Entradas---#
OpcionEscogidaNumero = int (input(preguntaNumero))
OpcionEscogidaMoneda = (input(preguntaMoneda))

while (OpcionEscogidaNumero !=4):
    #---Punto 1---#
    if (OpcionEscogidaNumero == 1):
        OpcionEscogidaMoneda = (input(preguntaMoneda))
        if (OpcionEscogidaMoneda == "D"):
            print("La conversion no es necesaria, su valor está en Dolares")
            print(listaDolares)
        elif(OpcionEscogidaMoneda == "C"):
            print("Mostrando lista en COP")
            print(listaPesos)
        elif(OpcionEscogidaMoneda == "E"):
            print("Mostrando lista en Euros")
            print(listaEuros)
        else:
            print("El valor ingresado no es valido")
    #---Punto 2---#
    elif (OpcionEscogidaNumero == 2):
        Ingreso = float(input(preguntaIngresos))
        if (Ingreso <= 1000 ):
            print("Sus ingresos al es se catalogan como bajos")
        elif (Ingreso > 1000 and Ingreso <= 7000):
            print("Sus ingresos al mes se catalogan como medios")
        elif(Ingreso >= 7000 and Ingreso < 20000):
            print("Sus ingresos al mes se catalogan como altos")
        else:
            print("Sus ingresos al mes se catalogan como elevados")
    #---Punto 3---#
    elif (OpcionEscogidaNumero == 3):
        print( "Este es el ingreso mayor : " , max ( listaDolares ))
        print("Este es el ingreso menor : " , min ( listaDolares ))
        print("Este es el promedio : " , sum ( listaDolares ) / len ( listaDolares ))
    #------opcion4-----#
    else:
        print("Esta opcion es invalida")
    OpcionEscogidaNumero = int(input(preguntaNumero))

print("Gracias por contar con nosotros")


