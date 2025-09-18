"PRUEBAS"
#----------------------------------#
# VIDEO 3
# Desarrollar un algoritmo que permita ingresar una cantidad de personas. La computadora debe
# pedir la edad de cada una y finalmente mostrar el porcentaje de personas que es mayor de edad.

personas=int(input("Ingrese cantidad de personas: "))
if personas <= 0:
    while personas < 0:
        personas=int(input("Ingrese cantidad válida de personas: "))
personas_mayores=0
for i in range(personas):
    edad=int(input(f"Ingrese la edad de la persona {i+1}: "))
    if edad >= 18:
        personas_mayores += 1
porcentaje_personas_mayores= (personas_mayores / personas) * 100
print("El porcentaje de personas mayores es de: ", round(porcentaje_personas_mayores,2), "porciento.")
