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
print(random[:-1])
