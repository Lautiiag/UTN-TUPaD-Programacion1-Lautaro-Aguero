"AUXILIAR"
#----------------------------------#

print("Ejercicio 5")
frase=input("Ingrese frase para mostrar palabras únicas de la misma: ")
frase_lista=frase.split()
frase_set=set(frase_lista)
print(frase_set)
