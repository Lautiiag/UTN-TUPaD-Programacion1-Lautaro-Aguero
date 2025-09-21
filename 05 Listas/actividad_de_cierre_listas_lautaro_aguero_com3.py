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
