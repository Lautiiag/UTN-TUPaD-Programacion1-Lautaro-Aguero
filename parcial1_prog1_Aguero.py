"Parcial 1"
titulos=[]
ejemplares=[]
salir=False

while salir == False: 
    print("--------BILBIOTECA--------")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar títulos y respectivos ejemplares")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")
    opcion=input("Ingrese una opción: ")

    match opcion:
        case "1": #Agregar nuevos títulos (con ejemplares=0)
            cant_titulos_agregar=int(input("Ingrese la cantidad de títulos a agregar: "))
            if cant_titulos_agregar > 0 or cant_titulos_agregar != "": #Valida que la cantidad sea positiva o 0 y que la línea no esté vacía. 
                for i in range(cant_titulos_agregar):
                    nuevo_titulo=input("Ingrese nuevo título: ").strip().lower()
                    if nuevo_titulo in titulos or nuevo_titulo == "" or not nuevo_titulo.isalpha(): #Valida que el título no se encuentre en la biblioteca y la línea no esté vacía.
                        print("El título ya se encuentra en la lista, dejó la línea vacía o ingresó un título con números.")
                        break
                    else:
                        titulos.append(nuevo_titulo)
                        ejemplares.append(0)
            else:
                print("La cantidad ingresada es negativa o la línea quedó vacía.")
                break
        case "2":
            for i in range(len(titulos)):
                cant_ejemplares=int(input(f"Ingrese cantidad de ejemplares de {titulos[i].title()}: "))
                if cant_ejemplares < 0 or cant_titulos_agregar == "": #Valida que la cantidad sea positiva o 0 y que la línea no esté vacía. 
                    print("La cantidad ingresada es negativa o la línea quedó vacía.")
                    break
                else:
                    ejemplares.append(cant_ejemplares)
        case "3":
            for i in range(len(titulos)):
                print("La cantidad de ejemplares de ", titulos[i].title(), "es de ", ejemplares[i], ".")
        case "4":
            titulo_cant_ejemp=print("Ingrese el titulo para saber la cantidad de ejemplares disponibles: ").strip().lower()
            if titulo_cant_ejemp in titulos or titulo_cant_ejemp != "" or not titulo_cant_ejemp.isalpha(): #Valida que el título se encuentre en la biblioteca y la línea no esté vacía.
                indice=titulos.index(titulo_cant_ejemp)
                print(f"Hay {ejemplares[indice]} ejemplares del titulo {titulos[indice].title()}.")
            else:
                print("El título no se encuentra en la biblioteca, la línea quedó vacía o ingresó un título con números.")
        case "5":
            for i in range(len(titulos)):
                if ejemplares[i] == 0:
                    print(f"El título {titulos[i]} no tiene ningún ejemplar. ")
                else:
                    print("No hay títulos sin ejemplares.")
        case "6":
            nuevo_titulo=input("Ingrese nuevo titulo: ").strip().lower()
            if nuevo_titulo in titulos or nuevo_titulo == "" or not nuevo_titulo.isalpha(): #Valida que el título no se encuentre en la biblioteca y la línea no esté vacía.
                print("El título ya se encuentra en la biblioteca o la línea quedó vacía.")
            else:
                titulos.append(nuevo_titulo)
                nueva_cant_ejemplares=int(input("Ingrese la cantidad de ejemplares: "))
                if nueva_cant_ejemplares < 0 or nueva_cant_ejemplares == "": #Valida que la cantidad sea positiva o 0 y que la línea no esté vacía. 
                    print("La cantidad de ejemplares ingresada es negativa o la línea quedó vacía")
                else:
                    ejemplares.append(nueva_cant_ejemplares)
        case "7":
            modificar_titulo=input("Ingrese el título a modificar: ").strip().lower()
            if not modificar_titulo in titulos or modificar_titulo == "" or not modificar_titulo.isalpha(): #Valida que el título no se encuentre en la biblioteca y la línea no esté vacía.
                print("El título no se encuentra en la biblioteca, la línea quedó vacía o ingresó un título con números.")
            indice_tit_mod=titulos.index(modificar_titulo)
            ejemplares_actualizados=int(input("Ingrese la cantidad de ejemplares actualizada: "))
            if ejemplares_actualizados < 0 or ejemplares_actualizados == "": #Valida que la cantidad sea positiva o 0 y que la línea no esté vacía. 
                print("La cantidad de ejemplares ingresada es negativa o la línea quedó vacía")
            else:
                ejemplares[indice_tit_mod]=ejemplares_actualizados
        case "8":
            salir=True
        case _:
            print("La opción ingresada no está disponible.")
            print()
