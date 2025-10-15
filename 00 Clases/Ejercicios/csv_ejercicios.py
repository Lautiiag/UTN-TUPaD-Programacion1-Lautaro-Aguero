"ejercicio csv"

import csv

def agregar_articulo(articulo, precio):
    with open("articulos.csv", "a", newline="") as archivo:
        escritor = csv.DictWriter(archivo)
        escritor.writerow([articulo, precio])

#CREAR ARCHIVO
articulos=[
    {"nombre":"manzana", "precio":"10"},
    {"nombre":"banana", "precio":"8"},
    {"nombre":"mandarina", "precio":"12"}]
with open("articulos.csv", "w", newline="") as archivo:
    campos = ["Artículo", "Precio"]
    escritor = csv.DictWriter(archivo, fieldnames = campos)
    escritor.writerow()
    escritor.writerow(articulos)


#INICIAR MENU
salir=False
while salir == False:
    print("1. Agregar artículo")
    print("2. Printear")
    print("3. Quitar artículo")

    print("9. Salir")

    opcion=input("Ingrese una opción: ")

    match opcion:
        case "1":
            articulo_global=input("Ingrese artículo: ").capitalize()
            precio_artículo=int(input("Ingrese valor: "))
            agregar_articulo(articulo_global, precio_artículo)
        case "2":
            with open("articulos.csv", "r") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    print(fila)
        case "3":
            articulo_a_eliminar=input("Ingrese el artículo: ")
            with open("articulos.csv", "r") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    if fila[1] != articulo_a_eliminar:
                        escritor = csv.writerow(fila)
        case "9":
            break
