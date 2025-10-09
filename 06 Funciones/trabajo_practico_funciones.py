"TRABAJO PRÁCTICO DE FUNCIONES"
###################### Definición de funciones ######################

#1.
def impirimir_hola_mundo(a):
    a="Hola Mundo!"
    print(a)

#2.
def saludar_usuario(nombre):
    print(f"¡Saludos {nombre}!")

#3.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4.
def calcular_area_circulo(radio):
    print("El área calculada con el radio ingresado es de: ", round((3.1415 * radio**2), 2), "metros.")
def calcular_perimetro_circulo(radio):
    print("El perímetro calculado con el radio ingresado es de: ", round((2 * 3.1415 * radio), 2), "metros." )

#5.
def segundos_a_horas(segundos):
    print(round((segundos/3600), 2))


###################### Programa Principal ######################

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
print("Ejercicio 1")
impirimir_hola_mundo(None)
print()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
print("Ejercicio 2")
saludar_usuario(input("¿Cómo es tu nombre? "))
print()


# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
# dir los datos al usuario y llamar a esta función con los valores in-
# gresados.
print("Ejercicio 3")
nombre_global=input("Ingrese su nombre: ")
apellido_global=input("Ingrese su apellido: ")
edad_global=int(input("Ingrese su edad: "))
residencia_global=input("Ingrese su residencia: ")
informacion_personal(nombre_global, apellido_global, edad_global, residencia_global)
print()


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
# dio como parámetro y devuelva el área del círculo. calcular_peri-
# metro_circulo(radio) que reciba el radio como parámetro y devuel-
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
# bas funciones para mostrar los resultados.
print("Ejercicio 4")
radio_global=float(input("Ingrese el radio en metros de la circunferencia: "))
calcular_area_circulo(radio_global)
calcular_perimetro_circulo(radio_global)
print()


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos-
# trar el resultado usando esta función.
print("Ejercicio 5")
segundos_a_horas(float(input("Ingrese cantidad de segundos: ")))
print()

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun-
# ción.
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta-
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
# sultados de forma clara.
# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales.
# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
