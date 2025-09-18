"PRUEBAS"
#----------------------------------#


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0

num1=1
suma1=0
while True:
    if num1 == 0:
        break
    num1=int(input("Ingrese un número entero para sumar: "))
    suma1= suma1 + num1
print(suma1)
