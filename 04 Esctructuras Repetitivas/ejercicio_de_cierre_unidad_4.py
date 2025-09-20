"Ejercicio de cierre de unidad 4"
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea
# EN ESTE EJERCICIO SE UTILIZA UNA VARIABLE PARA INDICAR EL NUMERO MAXIMO POR PRACTICIDAD.
print("EJERCICIO 1")

num_max=int(input("Ingrese el número entero máximo: "))
for i in range(0,num_max+1):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
print("EJERCICIO 2")

num=input("Ingrese un número entero: ")
print("El número tiene", len(num), "dígitos.")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
print("EJERCICIO 3")

minimo=int(input("Ingrese el valor mínimo: "))
maximo=int(input("Ingrese el valor máximo: "))
suma=0
for i in range(minimo+1,maximo):
    suma= suma + i
print("La suma es: ", suma)


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0
print("EJERCICIO 4")

num1=1
suma1=0
while True:
    if num1 == 0:
        break
    num1=int(input("Ingrese un número entero para sumar: "))
    suma1= suma1 + num1
print(suma1)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("EJERCICIO 5")
import random

numero_aleatorio=random.randint(0,9)
intentos=0
while True:
    num2=int(input("Ingrese un número: "))
    intentos += 1
    if num2 == numero_aleatorio:
        break
print("Intentos realizados: ", intentos)


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
print("EJERCICIO 6")
for i in range(100,-1,-2):
    print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
print("EJERCICIO 7")
numero_limite=int(input("Ingrese el número entero positivo límite: "))
suma=0
while numero_limite < 0:
    numero_limite=int(input("Intente nuevamente: "))
for i in range(numero_limite):
    suma=suma+i
print(suma)


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio)
print("EJERCICIO 8")

cantidad_numeros=int(input("Ingrese el número entero positivo límite: "))
while cantidad_numeros < 0:
    cantidad_numeros=int(input("Intente nuevamente: "))
contador_pares=0
contador_impares=0
contador_positivos=0
contador_negativos=0
for i in range(cantidad_numeros):
    num_ingresado=int(input(f"Ingrese el número {i+1} :"))
    if num_ingresado % 2 == 0:
        contador_pares +=1
    elif num_ingresado % 2 == 1:
        contador_impares +=1
    if num_ingresado > 0:
        contador_positivos +=1
    elif num_ingresado < 0:
        contador_negativos +=1

print(f"La cantidad de números pares es de: {contador_pares}")
print(f"La cantidad de números impares es de: {contador_impares}")
print(f"La cantidad de números positivos es de: {contador_positivos}")
print(f"La cantidad de números negativos es de: {contador_negativos}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
print("EJERCICIO 9")

acumulacion=0
cantidad_numeros=int(input("Ingrese el la cantidad máxima de números para la media: "))
for i in range(cantidad_numeros):
    numero_ingresado= int(input(f"Ingrese número {i+1}: "))
    acumulacion= acumulacion + numero_ingresado
media= acumulacion/cantidad_numeros
print(f"La media de los número es: {round(media,2)}.")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
print("EJERCICIO 10")

numero_a_invertir=input("Ingrese un número entero: ")
print(numero_a_invertir[::-1])
