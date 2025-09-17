"""trabajo_practico1_com3_lautaro_aguero"""

#### Este es mi primer codigo en Python, disculpas por errores visuales.
#### Agradecería si pudiera resaltarme algunas mejoras, gracias de antemano.
#### Me figura una sugerencia si una línea de código sobrepasa los 100 caracteres,?
#### Debería cambiarlo o dejarlo así?

#---------------------------------------------------------------------------------------------------
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!"
print("Hola Mundo!")


#---------------------------------------------------------------------------------------------------
#2)Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado.

nombre = input("Ingrese su nombre:")
print(f"Hola {nombre}!")


#---------------------------------------------------------------------------------------------------
#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados.

print("Ingrese los siguientes datos:")

nombre=input("Nombre: ")
edad=int(input("Edad: "))
residencia=input("Lugar de residencia: ")

print(f"Soy {nombre}, vivo en {residencia} y tengo {edad} años.")


#---------------------------------------------------------------------------------------------------
#4) Crear un programa que pida al usuario el radio de un círculo
# e imprima por pantalla su área y su perímetro.
####Tengo entendido que para involucrar a "Pi" en un código
# debe importarse una biblioteca, por eso utilizo 3.14.

radio=float(input("Ingrese radio de la circunferencia: "))
area=print("El area es: ", (3.14 * radio**2), ".")
perimetro=print("El perímetro es: ", 2 * 3.14 * radio,".")


#---------------------------------------------------------------------------------------------------
#5)Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos=float(input("Ingrese cantidad de segundos: "))
horas=print("El total de horas es: ", segundos/3600, ".")


#---------------------------------------------------------------------------------------------------
#6)Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número

numero=float(input("Ingrese un número: "))
print(numero*1)
print(numero*2)
print(numero*3)
print(numero*4)
print(numero*5)
print(numero*6)
print(numero*7)
print(numero*8)
print(numero*9)
print(numero*10)


#---------------------------------------------------------------------------------------------------
#7)Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1=float(input("Ingrese un primer numero distinto de 0: "))
while numero1 == 0:
    print("El numero no puede ser 0.")
    numero1=float(input("Ingrese un primer numero distinto de 0: "))


numero2=float(input("Ingrese un segundo numero distinto de 0: "))
while numero2 == 0:
    print("El numero no puede ser 0.")
    numero2=float(input("Ingrese un segundo numero distinto de 0: "))


print("La suma entre ambos números es: ", numero1 + numero2, ".")
print("La división entre ambos números es: ", numero1 / numero2, ".")
print("El producto entre ambos números es: ", numero1 * numero2, ".")
print("La resta entre ambos números es: ", numero1 - numero2, ".")


#---------------------------------------------------------------------------------------------------
#8)Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.
altura=float(input("Ingrese su altura en metros: "))
peso=float(input("Ingrese su peso en kilogramos: "))
print("Su índice de masa corporal es de: ", peso/(altura**2), ".")


#---------------------------------------------------------------------------------------------------
#9)Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit.
celsius=float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit= ((9/5)*celsius)+32
print("La temperatura en Fahrenheit es de:",fahrenheit, "grados.")


#---------------------------------------------------------------------------------------------------
#10)Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.


num1=float(input("Ingrese número 1:"))
num2=float(input("Ingrese número 2:"))
num3=float(input("Ingrese número 3:"))
promedio=print("El promedio es:",(num1+num2+num3)/3)



print("Fin del programa.")
