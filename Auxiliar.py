"AUXILIAR"
#----------------------------------#

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
def sacar_promedio(notas_tupla): #Saca promedios
    promedio=sum(notas_tupla) / len(notas_tupla)
    return promedio
def pedir_notas(cant_notas_funcion): #Pide la cantidad las notas para sacar promedio
    notas=[]
    for contador_notas in range(cant_notas_funcion):
        nota=float(input(f"Ingrese nota {contador_notas+1}: "))
        notas.append(nota) 
    return tuple(notas)

for i in range(3):
    nombre = input(f"Ingrese nombre del alumno {i+1}: ")
    notas = pedir_notas(3)
    promedio = sacar_promedio(notas)
    print(f"El promedio de {nombre} es de {round(promedio, 2)} puntos.\n")

