#---Taller 5---#
listaNumeros = [1,2,3,4,5,6,7,8,9,14,13,66,77,88]

#---Punto 1---#
for elemento in listaNumeros:
    print(elemento)

#---Punto 2---#
def Numeros ():
    print("Promedios en los numeros de la lista :")
    print("Este es el ingreso mayor : " , max ( listaNumeros ))
    print("Este es el ingreso menor : " , min (listaNumeros ))
    print("Este es el promedio : " , sum (listaNumeros ) / len (listaNumeros ))

Numeros()

#---Punto 3---#
def saludo (veces):
    for saludo in range (veces):
        print ("Bienvenido al código")

veces = int (input ("Ingrese número de veces que requiere un saludo :"))

saludo (veces)

#---Punto 4---#
def NumerosPares ():
    print("Numeros pares de la lista :")
    for Pares in listaNumeros : 
        if (Pares%2 == 0):
            print (Pares)

NumerosPares ()

#---Punto 5---#
def NumerosMayores ():
    print("Numeros mayores a 24 en la lista :")
    for Mayores in listaNumeros :
        if (Mayores > 24) :
            print (Mayores)

NumerosMayores()

#---Punto 6---#
def IMC (peso,estatura):
    imc = peso/(estatura**2)
    return (imc)

peso = float (input("Digite el peso :"))
estatura = float (input("Digite la estatura :"))

IMCpersonal = IMC(peso,estatura)
print("Su IMC es : ", IMCpersonal)

#---Punto 7---#
def Despedida (Nombre):
    print("Gracias por contar con nosotros", Nombre)

Nombre = input("Digite su nombre :")

Despedida(Nombre)