#-----Constantes-----#
PREGUNTA_PESO = "Cuanto pesas en kg? :"
PREGUNTA_ESTATURA = "Cuanto mides en mts? :"
MENSAJE_BIENVENIDA = "Hola como estas? voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es..."

#-----Entrada código-----#
print (MENSAJE_BIENVENIDA)
peso = float (input (PREGUNTA_PESO))
estatura = float (input (PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
isBajoPeso = imc < 18.5
isNormal = imc >= 18.5 and imc < 25 
isSobrePeso = imc >= 25 and imc < 30
resultado = ""
if (isBajoPeso):
    resultado = MENSAJE_BAJO_PESO
elif (isNormal) :
    resultado = MENSAJE_NORMAL
elif (isSobrePeso) :
    resultado = MENSAJE_SOBRE_PESO
else :
    resultado = MENSAJE_OBESO
print (MENSAJE_DESPEDIDA, imc)
print (resultado)