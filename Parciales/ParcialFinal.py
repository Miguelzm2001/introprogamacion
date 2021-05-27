#-----Examen parcial final-----#

#---Punto 1---#

import matplotlib.pyplot as plt
import pandas as pd 

Alimento1 = input("Ingresa uno de tus alimentos preferidos: ")
Precio1 = int(input("Ingresa el precio de este alimento: "))
Alimento2 = input("Ingresa uno de tus alimentos preferidos: ")
Precio2 = int(input("Ingresa el precio de este alimento: "))
Alimento3 = input("Ingresa uno de tus alimentos preferidos: ")
Precio3 = int(input("Ingresa el precio de este alimento: "))
Alimento4 = input("Ingresa uno de tus alimentos preferidos: ")
Precio4 = int(input("Ingresa el precio de este alimento: "))
Alimento5 = input("Ingresa uno de tus alimentos preferidos: ")
Precio5 = int(input("Ingresa el precio de este alimento: "))
Alimento6 = input("Ingresa uno de tus alimentos preferidos: ")
Precio6 = int(input("Ingresa el precio de este alimento: "))
Alimento7 = input("Ingresa uno de tus alimentos preferidos: ")
Precio7 = int(input("Ingresa el precio de este alimento: "))
Alimento8 = input("Ingresa uno de tus alimentos preferidos: ")
Precio8 = int(input("Ingresa el precio de este alimento: "))

ListaAlimento = [Alimento1, Alimento2, Alimento3, Alimento4, Alimento5, Alimento6, Alimento7, Alimento8]
ListaPrecios = [Precio1, Precio2, Precio3, Precio4, Precio5, Precio6, Precio7, Precio8]

plt.bar(ListaAlimento, ListaPrecios)
plt.xlabel("alimentos")
plt.ylabel("Precio")
plt.title("Grafica de alimentos favoritos")
plt.savefig("Graficoalimentos.png")
plt.show()

#---Punto 2---#
class Humano():
    def __init__(self, Nombre, Sexo, Edad):
        self.Nombre = Nombre
        self.Sexo = Sexo
        self.Edad = Edad
    def Hablar (self, Mensaje):
        print (Mensaje)


Humano1 = Humano ( "Miguel", "Masculino", 19)
Humano1.Hablar ("Hola, buenos días profe, lo queremos")

class Doctor(Humano):
    def __init__(self, Nombre, Sexo, Edad):
        self.Nombre = Nombre
        self.Sexo = Sexo
        self.Edad = Edad
    def IMC(self, peso, estatura): 
        imc = peso/(estatura**2)
        print(f"El IMC del paciente es {imc}")


Doctor1 = Doctor ("Miguel", "Masculino", 30)
Doctor1.IMC (72, 1.80)

#---Punto 3---#

def Conversoreurosendolares():
    isCorrectInfo = False
    while (isCorrectInfo == False):
        try:
            Nombre = input("Ingrese su nombre: ")
            assert (Nombre.isalpha())
            isCorrectInfo = True
        except AssertionError:
            print ("Ingresaste un dato no válido")

    isCorrectInfo = False
    while (isCorrectInfo == False):
        try:
            Dinero = float(input("Ingrese cantidad de dinero en dólares: "))
            isCorrectInfo = True
        except ValueError:
            print ("Ingresaste un dato no válido")

    print(f"Buenos días {Nombre}, la cantidad de dinero que tienes en euros es {Dinero*0.82}")
    Conversoreurosendolares()

input ("\n Presione una tecla para continuar")

#---Punto 4---#

NombreArchivo = "Paciente.txt"

try:
    Archivo = open (NombreArchivo)
except FileNotFoundError:
    Archivo = open (NombreArchivo, "w", encoding="UTF-8")
    DescripcionArchivo = "Archivo de pacientes neurologicos"
    Archivo.writelines (DescripcionArchivo)
    Archivo.close()

Nombre = input ("Digite su nombre :")
Enfermedad = input ("Digite la enfermedad que está padeciendo :")
Precio = 0

isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        ValorConsulta = int (input("Ingrese valor de su consulta: "))
        isCorrectInfo = True
    except ValueError:
        print ("Ingrese un dato no válido")

Archivo = open (NombreArchivo, "a", encoding = "UTF-8")
Archivo.write (f"Equipo : {Nombre}\n")
Archivo.write (f"Descripcion : {Enfermedad}\n")
Archivo.write (f"Precio : {ValorConsulta}\n")
Archivo.write ("==============\n")
Archivo.close()



