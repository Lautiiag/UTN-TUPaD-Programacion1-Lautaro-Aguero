"PRUEBAS"
#----------------------------------#
import random

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

numero_aleatorio=random.randint(0,9)
intentos=0
while True:
    num2=int(input("Ingrese un número: "))
    intentos += 1
    if num2 == numero_aleatorio:
        break
print("Intentos realizados: ", intentos)
