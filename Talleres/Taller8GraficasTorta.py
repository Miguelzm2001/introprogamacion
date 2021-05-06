#---Taller 8---#
#--Torta---#

import matplotlib.pyplot as plt
pielabels = ["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena"]
sizes = [11.7, 6.7, 4.5, 4.3, 3.3]
pieExplode = [0.1, 0, 0, 0, 0]

plt.pie (sizes, labels = pielabels, explode = pieExplode, shadow = True,counterclock = True, startangle = 45 )
plt.title ("Grafico de ciudades poblacionalmente más grandes de Colombia")
plt.savefig ("GraficoTorta.png")
plt.show()
