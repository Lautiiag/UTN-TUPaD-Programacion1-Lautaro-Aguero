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
    print("Desaprobado")


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
print(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("El sesgo es positivo.")
elif media < mediana and mediana < moda:
    print("El sesgo es negativo.")
else:
    print("Sin sesgo.")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase=input("Ingrese una frase o palabra: ").lower().strip()
vocal=("a","e","i","o","u")
if frase.endswith(vocal):
    print(frase + "!")
else:
    print(frase)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla.

nombre=input("Ingrese su nombre: ")
print("Ingrese una opción:")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion=int(input(""))

if opcion == 1 :
    nombre=nombre.upper()
    print(nombre)
elif opcion == 2 :
    nombre=nombre.lower()
    print(nombre)
elif opcion == 3:
    nombre=nombre.title()
    print(nombre)


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)

magnitud=float(input("Ingrese la magnitud del terremoto (escala Ritcher): "))
if magnitud < 3 :
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4 :
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5 :
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6 :
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7 :
    print("Muy fuerte (puede causar daños significativos).")
elif magnitud >= 7 :
    print("Extremo (puede causar graves daños a gran escala).")


# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
# ------------(en este punto no concideré validaciones porque no se me ocurre cómo realizarlas sin
# utilizar un while-try)

hemisferio=input("En qué hemisferio se encuentra (N/S)?").lower()
mes=int(input("En qué número de mes se encuentra?"))
dia=int(input("Que dia es?"))

if hemisferio == "s" :
    # Este bloque es de verano.
    if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
        print("Usted se encuentra en verano.")
    # Este bloque es de otoño.
    elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
        print("Usted se encuentra en otoño.")
    # Este bloque es de invierno.
    elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
        print("Usted se encuentra en invierno.")
    # Este bloque es de primavera.
    elif (mes == 9 and dia >= 21) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
        print("Usted se encuentra en primavera.")
elif hemisferio == "n" :
    # Este bloque es de invierno.
    if (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
        print("Usted se encuentra en invierno.")
    # Este bloque es de primavera.
    elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
        print("Usted se encuentra en primavera.")
    # Este bloque es de verano.
    elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
        print("Usted se encuentra en verano.")
    # Este bloque es de otoño.
    elif (mes == 9 and dia >= 21) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
        print("Usted se encuentra en otoño.")
