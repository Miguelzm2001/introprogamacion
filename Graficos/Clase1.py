#Aqui explicaremos como hacer un gráfico de barras
import matplotlib.pyplot as plt 
lenguajes = ["py", "java", "darts", "ts", "elixir"]
encuesta = [50,10,20,10,10]
plt.bar(lenguajes, encuesta) 
################
#Titulo
plt.title ("Lenguajes mas usados")
plt.xlabel ("Lenguajes de programacion")
plt.ylabel ("% de uso de lenguajes")
plt.savefig ("GraficoLenguaje.png")
################
plt.show() 