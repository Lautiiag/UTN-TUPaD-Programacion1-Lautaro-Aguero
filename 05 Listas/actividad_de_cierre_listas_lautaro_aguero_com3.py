"Ejercicio de cierre de unidad 5"

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.
print("Ejercicio 01")

num_limite=int(input("Ingrese número límite: "))
for i in range(0,num_limite,4):
    print(i,end=", ")


# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!
print("Ejercicio 02")

random=["UTN", "Lauti",1,True,2.15,"Último"]
print(random[(len(random)-1)])


# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla.
print("Ejercicio 03")

lista_vacia=[]
lista_vacia.append("Lautaro")
lista_vacia.append("Agustín")
lista_vacia.append("Agüero")

print(lista_vacia)


# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
print("Ejercicio 04")

animales = ["perro", "gato", "conejo", "pez"]
animales[1]="loro"
animales[(len(animales)-1)]="oso"
print(animales)


# # 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros=[0,15,3,22,7]
# numeros.remove(max(numeros))
# print(numeros)
print("Ejercicio 05")

# Prueba de análisis
numeros=[0,15,3,22,7]
print(numeros)
numeros.remove(max(numeros))
print(numeros)

# Respuesta: El código elimina el valor más alto dentro de la lista, en este caso 22.


# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.
print("Ejercicio 06")

lista_paso_5=[10,15,20,25,30]
print(lista_paso_5[0:2])


# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
print("Ejercicio 07")

autos = ["sedan", "polo", "suran", "gol"]
autos[1]="mustang"
autos[2]="raptor"
print(autos)


# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla
print("Ejercicio 03")

dobles=[]
dobles.append(10)
dobles.append(20)
dobles.append(30)
print(dobles)


# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla
print("Ejercicio 09")

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

compras[2].append("jugo")

compras[1][1]="tallarines"

del compras[0][0]

print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada=[[15],[True],[25.5, 57.9, 30.6],[False]]

print(lista_anidada)
