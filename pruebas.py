"PRUEBAS"
#----------------------------------#

# VIDEO 04
# Desarrollar un algoritmo que permita ingresar el nombre y la edad (por separado) de diferentes personas. 
# La carga termina cuando en el nombre de la próxima persona se ingresa un asterisco (*). 
# La computadora debe mostrar como se llama la persona más joven

edad_minima = float("inf")
nombre_persona_joven = ""
edad_persona_joven = 0

while True:
    nombre = input("Ingrese nombre de la persona: ")
    if "*" in nombre:
        break

    edad2 = int(input("Ingrese edad de la persona: "))
    while edad2 <= 0:
        edad2 = int(input("Ingrese una edad válida (mayor a 0): "))

    if edad2 < edad_minima:
        edad_minima = edad2
        nombre_persona_joven = nombre
        edad_persona_joven = edad2

print(nombre_persona_joven.title(), "es la persona más joven.")
