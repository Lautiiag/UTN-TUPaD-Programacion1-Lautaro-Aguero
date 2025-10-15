"Tp Datos complejos"

def agregar_elementos_a_diccionario(nombre_diccionario,cantidad_elementos,key,value):
    nombre_diccionario[key]=value

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

#############FALTA TERMINARRRRRRRRRRRRR##############
