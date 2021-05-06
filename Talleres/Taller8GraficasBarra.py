#---Taller 8---#
#--Barra--#

import matplotlib.pyplot as plt
Mes = ["Enero", "Marzo", "Mayo", "Julio", "Septiembre", "Noviembre"]
Ingresos = [700, 689, 900, 830, 790, 879]
plt.bar (Mes, Ingresos, width = 0.8, color = "r")
plt.title ("Cantidad de ingresos")
plt.xlabel ("Mes")
plt.ylabel("Ingresos")
plt.savefig("GraficoBarra.png")
plt.show()
