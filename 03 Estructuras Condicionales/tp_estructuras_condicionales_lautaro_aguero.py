"Trabajo Práctico Condicionales Unidad 03 Lautaro Agustín Agüero"
from statistics import mode, median, mean
import random
# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    pass


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota_usuario=float(input("Ingrese su nota: "))
if nota_usuario >= 6:
    print("Aprobado")
else:
    print("Desaprovado")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

num_usuario=int(input("Ingrese un número par: "))
if num_usuario % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años

edad_usuario=int(input("Ingrese su edad: "))
if edad_usuario < 12:
    print("Niño/a.")
elif edad_usuario >= 12 and edad_usuario < 18:
    print("Adolescente.")
elif edad_usuario >= 18 and edad_usuario < 30:
    print("Adulto/a joven.")
elif edad_usuario >= 30:
    print("Adulto/a.")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

contra=input("Ingrese una contraseña entre 8 y 14 caracteres: ")
if len(contra) >= 8 and len(contra) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6)escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.


numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media=mean(numeros_aleatorios)
moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("El sesgo es positivo.")
elif media < mediana and mediana < moda:
    print("El sesgo es negativo.")
else:
    print("Sin sesgo.")
