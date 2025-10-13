"ejercicio csv"

import csv

def agregar_articulo(articulo, precio):
    with open("alumnos.csv", "a", newline="") as archivo:
        escritor = csv.DictWriter(archivo)
        escritor.writerow([articulo, precio])

#CREAR ARCHIVO
with open("alumnos.csv", "w", newline="") as archivo:
    escritor = csv.DictWriter(archivo)
    escritor.writerow(["Articulo", "Precio"])  # encabezado
    escritor.writerow(["Banana", 10])
    escritor.writerow(["Pera", 15])
    escritor.writerow(["Manzana", 12])

#INICIAR MENU
salir=False
while salir == False:
    print("1. Agregar arículo")
    print("2. Printear")
    print("9. Salir")

    opcion=input("Ingrese una opción: ")

    match opcion:
        case "1":
            articulo_global=input("Ingrese artículo: ").capitalize()
            precio_artículo=int(input("Ingrese valor: "))
            agregar_articulo(articulo_global, precio_artículo)
        case "2":
            with open("alumnos.csv", "r") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    print(fila)
        case "3":
            agregar_articulo(0,0)
        case "9":
            break
