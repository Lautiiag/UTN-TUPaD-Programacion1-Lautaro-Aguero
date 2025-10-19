"Tp Datos complejos"
#------------------FUNCIONES
#Ejercicio 4
def agregar_elementos_a_diccionario(nombre_diccionario,cantidad_elementos,key,value):
    nombre_diccionario[key]=value
#Ejercicio 6
def sacar_promedio(notas_tupla): #Saca promedios
    promedio=sum(notas_tupla) / len(notas_tupla)
    return promedio
def pedir_notas(cant_notas_funcion): #Pide la cantidad las notas para sacar promedio
    notas=[]
    for contador_notas in range(cant_notas_funcion):
        nota=float(input(f"Ingrese nota {contador_notas+1}: "))
        notas.append(nota) 
    return tuple(notas)

#------------------RESOLUCION DE PROBLEMAS

# 1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
print("Ejercicio 1")
precios_frutas = {
'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450
}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
print("Ejercicio 2")
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
print("Ejercicio 3")
frutas=[precios_frutas.keys()]

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
print("Ejercicio 4")
numeros_telefonicos={
}
for elementos_agregados in range(5):
    nombre_contacto=input("Ingrese nombre del contacto: ")
    numero_contacto=int(input("Ingrese número del contacto: "))
    agregar_elementos_a_diccionario(numeros_telefonicos,5,nombre_contacto,numero_contacto)
nombre_a_buscar=input("Ingrese nombre a buscar: ")
if nombre_a_buscar in numeros_telefonicos:
    print(f"El número del contacto es: {numeros_telefonicos[nombre_a_buscar]}.")
else:
    print("El contacto no existe en la lista.")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
print("Ejercicio 5")
frase=input("Ingrese frase para mostrar palabras únicas de la misma: ")
frase_lista=frase.split()
frase_set=set(frase_lista)
print(frase_set)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
print("Ejercicio 6")

for i in range(3):
    nombre = input(f"Ingrese nombre del alumno {i+1}: ")
    notas = pedir_notas(3)
    promedio = sacar_promedio(notas)
    print(f"El promedio de {nombre} es de {round(promedio, 2)} puntos.\n")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
print("Ejercicio 7")
aprobados_parcial1={"Pepe","Agustín","Jorge","Nahuel","Pedro","Facundo"}
aprobados_parcial2={"Matias","José","Jorge","Agusto","Pedro","Facundo"}

ambos_parciales = aprobados_parcial1 & aprobados_parcial2
solo_uno = aprobados_parcial1 ^ aprobados_parcial2
al_menos_uno = aprobados_parcial1 | aprobados_parcial2

print("Alumnos que aprobaron ambos parciales:")
print(*ambos_parciales, sep=", ")

print("Alumnos que aprobaron solo uno de los dos:")
print(*solo_uno, sep=", ")

print("Alumnos que aprobaron al menos un parcial (sin repetir):")
print(*al_menos_uno, sep=", ")

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
# Diccionario de productos con su stock
print("Ejercicio 8")
productos = {
    "leche": 10,
    "pan": 25,
    "arroz": 15,
}

# Mostrar productos disponibles
print("Productos disponibles actualmente:")
for nombre, stock in productos.items():
    print(f"- {nombre}: {stock} unidades")

# Solicitar producto al usuario
producto = input("Ingrese el nombre del producto que desea consultar: ").lower()

# Verificar si el producto existe en el diccionario
if producto in productos:
    print(f"El producto '{producto}' tiene {productos[producto]} unidades en stock.")

    # Consultar si desea agregar más unidades
    opcion = input("¿Desea agregar unidades a este producto? (s/n): ").lower()
    if opcion == "s":
        cantidad = int(input("Ingrese la cantidad a agregar: "))
        productos[producto] += cantidad
        print(f"Se agregaron {cantidad} unidades. Nuevo stock de '{producto}': {productos[producto]} unidades.")
    else:
        print("No se modificó el stock.")

else:
    print(f"El producto '{producto}' no existe en el inventario.")
    opcion = input("¿Desea agregarlo al diccionario? (s/n): ").lower()
    if opcion == "s":
        cantidad = int(input("Ingrese la cantidad inicial de stock: "))
        productos[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")
    else:
        print("No se agregó el producto.")

# Mostrar diccionario actualizado
print("Stock actualizado de productos:")
for nombre, stock in productos.items():
    print(f"- {nombre}: {stock} unidades")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.
print("Ejercicio 9")

# Agenda con algunos eventos de ejemplo
agenda = {
    ("lunes", "10:00"): "Reunión de trabajo",
    ("martes", "15:30"): "Ir al gimnasio",
    ("jueves", "09:00"): "Dentista",
}

# Mostrar agenda actual
print("Agenda actual:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"- {dia.capitalize()} a las {hora}: {evento}")

# Consultar un día y hora
print("\nConsultar evento")
dia_consulta = input("Ingrese el día: ").lower()
hora_consulta = input("Ingrese la hora (formato HH:MM): ")

# Crear la tupla con los datos ingresados
clave_busqueda = (dia_consulta, hora_consulta)

# Verificar si existe en la agenda
if clave_busqueda in agenda:
    print(f"\nEn {dia_consulta.capitalize()} a las {hora_consulta} hay: {agenda[clave_busqueda]}")
else:
    print(f"\nNo hay ningún evento agendado el {dia_consulta.capitalize()} a las {hora_consulta}.")
    opcion = input("¿Desea agregar un evento en esa fecha y hora? (s/n): ").lower()
    if opcion == "s":
        nuevo_evento = input("Ingrese el nombre del evento: ")
        agenda[clave_busqueda] = nuevo_evento
        print(f"Evento '{nuevo_evento}' agregado correctamente.")
    else:
        print("No se agregó ningún evento.")

# Mostrar agenda actualizada
print("\nAgenda actualizada:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"- {dia.capitalize()} a las {hora}: {evento}")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
print("Ejercicio 10")

paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia",
    "Paraguay": "Asunción"
}

# Mostrar diccionario original
print("Diccionario original (países → capitales):")
for pais, capital in paises_a_capitales.items():
    print(f"- {pais}: {capital}")

# Crear nuevo diccionario (capitales → países)
capitales_a_paises = {}
for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais

# Mostrar nuevo diccionario invertido
print("\nNuevo diccionario (capitales → países):")
for capital, pais in capitales_a_paises.items():
    print(f"- {capital}: {pais}")
