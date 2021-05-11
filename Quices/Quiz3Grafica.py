#----Quiz 3 Grafico----#

#---Punto 1---#

import matplotlib.pyplot as plt
import pandas as pd 

Snack1 = input("Ingresa uno de tus Snacks preferidos: ")
Precio1 = int(input("Ingresa el precio de este snack: "))
Snack2 = input("Ingresa uno de tus Snacks preferidos: ")
Precio2 = int(input("Ingresa el precio de este snack: "))
Snack3 = input("Ingresa uno de tus Snacks preferidos: ")
Precio3 = int(input("Ingresa el precio de este snack: "))
Snack4 = input("Ingresa uno de tus Snacks preferidos: ")
Precio4 = int(input("Ingresa el precio de este snack: "))
Snack5 = input("Ingresa uno de tus Snacks preferidos: ")
Precio5 = int(input("Ingresa el precio de este snack: "))

ListaSnacks = [Snack1, Snack2, Snack3, Snack4, Snack5]
ListaPrecios = [Precio1, Precio2, Precio3, Precio4, Precio5]

plt.bar(ListaSnacks, ListaPrecios)
plt.xlabel("Snacks")
plt.ylabel("Precio")
plt.title("Grafica de Snacks")
plt.savefig("GraficoSnacks.png")
plt.show()

#---Punto 2---#

Ciudad1 = input("Ingresa una de tus ciudades favoritas en el mundo: ")
Poblacion1 = int(input("Ingresa la poblacion de esta cuidad: "))
Ciudad2 = input("Ingresa una de tus ciudades favoritas en el mundo: ")
Poblacion2 = int(input("Ingresa la poblacion de esta cuidad: "))
Ciudad3 = input("Ingresa una de tus ciudades favoritas en el mundo: ")
Poblacion3 = int(input("Ingresa la poblacion de esta cuidad: "))
Ciudad4 = input("Ingresa una de tus ciudades favoritas en el mundo: ")
Poblacion4 = int(input("Ingresa la poblacion de esta cuidad: "))
Ciudad5 = input("Ingresa una de tus ciudades favoritas en el mundo: ")
Poblacion5 = int(input("Ingresa la poblacion de esta cuidad: "))

ListaCiudades = [Ciudad1, Ciudad2, Ciudad3, Ciudad4, Ciudad5]
ListaPoblaciones = [Poblacion1, Poblacion2, Poblacion3, Poblacion4, Poblacion5]

plt.pie(ListaPoblaciones, labels=ListaCiudades)
plt.title("Grafico Ciudades en el mundo")
plt.savefig("GraficoCiudades.png")
plt.show()

#---Punto 3---#

print("ECG:Representación visual de la actividad eléctrica del corazón en función del tiempo")
print("PPG; La fotopletismografía es una técnica de pletismografía donde se utiliza un haz de luz para determinar el volumen de un órgano.")

df = pd.read_csv("ecg.csv", sep=";")
ValorECG = df["Valor"]

plt.plot(ValorECG)
plt.title("Grafica Electrocardiograma")
plt.xlabel("Tiempo")
plt.ylabel("mV")
plt.savefig("GraficaECG.png")
plt.show()

df2 = pd.read_csv("ppg.csv", sep=";")
ValorPPG = df2["Valor"]

plt.plot(ValorPPG)
plt.title("Grafica fotopletismografía ")
plt.xlabel("Tiempo")
plt.ylabel("Volumen")
plt.savefig("GraficaPPG.png")
plt.show()