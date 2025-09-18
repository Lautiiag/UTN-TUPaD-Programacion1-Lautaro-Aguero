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
