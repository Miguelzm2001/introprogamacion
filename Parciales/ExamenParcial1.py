#---PARCIAL 1---#

#---Punto 1---#
print ("#"*15, "Punto 1", "#"*15)

def sumar (a = 0, b = 0, c = 0):
    suma = a + b + c
    return suma

def restar (a = 0, b = 0, c = 0):
    resta = a - b - c
    return resta

def multiplicar (a = 0, b = 0, c = 0):
    multiplicar = a * b * c
    return multiplicar

def dividir (a = 0, b = 1, c = 1):
    division = a / b / c
    return division

def potenciar (base = 0, a = 1, b = 1):
    potencia = base ** a ** b
    return potencia

def Operaciones (Operaciones, a, b, c,):
    print(Operaciones(a,b,c))

Operaciones (sumar, 8,9,7)
Operaciones (restar, 7,3,6)
Operaciones (multiplicar, 8,4,6)
Operaciones (dividir, 88,6,4)
Operaciones (potenciar, 3,4,5)

#---Punto 2---#
print ("#"*15, "Punto 2", "#"*15)
Lista1 = [1,2,3,4,5,6]
Lista2 = [6,7,9,5,6,8]
Lista3 = [5,7,8,4,2,1]

print ("#"*6, "Lista 1", "#"*6)

def Lista():
    for elemento in Lista1:
        print(elemento)

Lista()

print ("#"*6, "Lista 2", "#"*6)

def Listado():
    for elemento in Lista2:
        print(elemento)

Listado()

print ("#"*6, "Lista 3", "#"*6)

def OtraLista():
    for elemento in Lista3:
        print (elemento)

OtraLista()


#---Punto 3---#
print ("#"*15, "Punto 3", "#"*15)
def Area (base,altura):
    Area = (base * altura)/2
    return Area

base = float (input("Digite la base :"))
altura = float (input("Digite la altura :"))

ElAreaBuscada = Area (base,altura)
print ("El area obtenida es :", ElAreaBuscada)

#---Punto 4---#
print ("#"*15, "Punto 4", "#"*15)
def lista ():
    print("Listas de numeros con sus respectivas medidas :")
    print("Este es el ingreso mayor : " , max ( Lista1 ))
    print("Este es el ingreso menor : " , min (Lista1 ))
    print("Este es el promedio : " , sum (Lista1 ) / len (Lista1 ))

lista()

#---Punto 5---#
print ("#"*15, "Punto 5", "#"*15)
ListaFibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

def MostrarLista (Valor):
    Valor1 = 0
    Valor2 = 1
    for elemento in range (Valor - 1):
        Listado = Valor1 + Valor2
        Valor1 = Valor2
        Valor2 = Listado
    return (Valor1)
posicion = MostrarLista(7)

print("Numero solicitado en lista Fibonacci :", posicion)



