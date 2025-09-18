"Ejercicios Actividad Número 3 Unidad 4"

# VIDEO 1
# Desarrollar un algoritmo que permita ingresar un número entero positivo. La computadora debe
# mostrar la sucesión de números pares desde el número ingresado hasta el cero (inclusive), en una
# sola línea. Ejemplo: Si ingresa 15, debe mostrar: 14 12 10 8 6 4 2 0

num=int(input("Ingrese un número entero positivo: "))
if num <= 0:
    while num <= 0:
        num=int(input("Por favor ingrese un número entero positivo: "))
for num in range(num,-1,-1):
    if num % 2 == 0:
        print(num, end=" ")


# VIDEO 2
# Desarrollar un algoritmo que permita ingresar un número entero entre 1 y 10 (inclusive). La
# computadora debe mostrar la tabla de multiplicar del número ingresado.
# Ejemplo: Si ingresa 7, debe mostrar:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

num2=int(input("Ingrese un número entero entre 1 y 10 (inclusive): "))
for i in range(11):
    resultado=i*num2
    print(f"{num2} x {i} = {resultado}")


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
