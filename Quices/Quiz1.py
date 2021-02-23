#---Quiz 1---#

print ("#"*15, "Triglicéridos", "#"*15)
#---Constantes---#
MENSAJE_BIENVENIDA = "Hola, como estas? Recuerda cuidarte"
PREGUNTA_TRIGLICÉRIDOS = "Digita nivel de triglicéridos :"
PREGUNTA_HOMOCISTEÍNA = "Digita nivel de homocisteíma :"

#---Entrada de código---#
print (MENSAJE_BIENVENIDA)
triglicéridos = int (input(PREGUNTA_TRIGLICÉRIDOS))
isÓptimo = triglicéridos < 150
isSobreLimite = triglicéridos >= 150 and triglicéridos < 199
isAlto = triglicéridos >= 200 and triglicéridos < 499
isMuyAlto = triglicéridos >= 500

#---Código---#
if(isÓptimo):
    print ("El nivel de triglicéridos ingresado es óptimo, recuerda revisarte periódicamente")
elif(isSobreLimite):
    print ("El nivel de triglicéridos ingresado está sobre el límite, ten precaución con ello")
elif(isAlto):
    print ("El nivel de triglicéridos ingresado es alto, informa al profesional en el área")
else:
    print ("El nivel de triglicéridos ingresado es muy alto, acude con brevedad al profesional en el área") 


print ("#"*15, "Homocisteína", "#"*15)

#---Entrada de código---#
homocisteína = int (input(PREGUNTA_HOMOCISTEÍNA))
isÓptimo = homocisteína >= 2 and homocisteína < 15
isSobreLimite = homocisteína >= 15 and homocisteína < 30
isAlto = homocisteína >= 30 and homocisteína < 10
isMuyAlto = homocisteína >= 100

#---Código---#
if(isÓptimo):
    print ("El nivel de homocisteína ingresado es óptimo, recuerda revisarte periódicamente")
elif(isSobreLimite):
    print ("El nivel de homocisteína ingresado está sobre el límite, ten precaución con ello")
elif(isAlto):
    print ("El nivel de homocisteína ingresado es alto, informa al profesional en el área")
else:
    print ("El nivel de homocisteína ingresado es muy alto, acude con brevedad al profesional en el área") 
