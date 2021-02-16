saludo = "Hola Mundo"
#Estos son mis datos personales
Nombre = "Miguel"
Edad = 19
Peso = 70
Estatura = 1.80
pruebaV = True
pruebaF = False
pruebaV = pruebaF
#Empezaremos a generar preguntas con sus respectivas respuestas
print ("#"*15, "Estatura promedio", "#"*15 )
isEstaturapromedio = Estatura >= 1.70
print (isEstaturapromedio)
print ("Mi estatura es mayor al promedio", "mido", Estatura)
print ("#"*15, "Tengo edad para sacar pase de conducción", "#"*15 )
isEdadparaconducir = Edad  >=16
print(isEdadparaconducir)
print ("Soy mayor a 16 años", "tengo", Edad)
print ("#"*15, "Tengo peso saludable", "#"*15 )
#Un peso saludable se define teniendo en cuenta la estatura de la persona 
isPesosaludable = Peso <= 100
print (isPesosaludable)
print ("#"*15, "Me llamo Miguel", "#"*15 )
isMinombreMiguel = Nombre >= Nombre
print (isMinombreMiguel)

#Datos familiares
EdadMadre = 42
EdadPadre = 46
isMayormadrequepadre = EdadMadre > EdadPadre
print (isMayormadrequepadre )
isDiferenciadeedad = EdadPadre - EdadMadre
print (isDiferenciadeedad)
isEdadalserpadres = EdadPadre - Edad, EdadMadre - Edad
print (isEdadalserpadres)