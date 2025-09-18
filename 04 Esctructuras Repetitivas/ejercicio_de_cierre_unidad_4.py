"Ejercicio de cierre de unidad 4"
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea
# EN ESTE EJERCICIO SE UTILIZA UNA VARIABLE PARA INDICAR EL NUMERO MAXIMO POR PRACTICIDAD.

num_max=int(input("Ingrese el número entero máximo: "))
for i in range(0,num_max+1):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num=input("Ingrese un número entero: ")
print("El número tiene", len(num), "dígitos.")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

minimo=int(input("Ingrese el valor mínimo: "))
maximo=int(input("Ingrese el valor máximo: "))
suma=0
for i in range(minimo+1,maximo):
    suma= suma + i
print("La suma es: ", suma)

