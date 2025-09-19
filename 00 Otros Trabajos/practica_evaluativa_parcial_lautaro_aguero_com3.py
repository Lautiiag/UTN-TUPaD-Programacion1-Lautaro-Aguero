# Práctica Evaluativa –Parcial I. Lautaro Agustín Agüero, Comisión 3.
# Inicialización de listas
titulos = []
ejemplares = []

salir = False
while not salir:
    print("\n Biblioteca")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar títulos agotados")
    print("6. Agregar un título")
    print("7. Préstamo o devolución")
    print("8. Salir")

    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        agregar = "s"
        while agregar == "s":
            titulo_nuevo = input("Ingrese el título: ").strip()
            if titulo_nuevo == "":
                print("El título no puede estar vacío.")
            else:
                repetido = False
                for t in titulos:
                    if t.lower() == titulo_nuevo.lower():
                        repetido = True
                if repetido:
                    print("El título ya existe en la biblioteca.")
                else:
                    titulos.append(titulo_nuevo)
                    ejemplares.append(0)
                    print("Título agregado con éxito.")
            agregar = input("¿Desea agregar otro título? (s/n): ").strip().lower()

    elif opcion == 2:
        if len(titulos) == 0:
            print("No hay títulos cargados.")
        else:
            for i in range(len(titulos)):
                while True:
                    try:
                        cant = int(input(f"Ingrese cantidad de ejemplares para '{titulos[i]}': "))
                        if cant < 0:
                            print("La cantidad no puede ser negativa.")
                        else:
                            ejemplares[i] = cant
                            break
                    except ValueError:
                        print("Por favor, ingrese un número entero válido.")

    elif opcion == 3:
        if len(titulos) == 0:
            print("No hay títulos en la biblioteca.")
        else:
            print("\nCatálogo de la biblioteca:")
            for i in range(len(titulos)):
                print(f"{titulos[i]} - {ejemplares[i]} ejemplares")

    elif opcion == 4:
        if len(titulos) == 0:
            print("No hay títulos en la biblioteca.")
        else:
            consulta = input("Ingrese el título a consultar: ").strip()
            encontrado = False
            for i in range(len(titulos)):
                if titulos[i].lower() == consulta.lower():
                    print(f"'{titulos[i]}' tiene {ejemplares[i]} ejemplares disponibles.")
                    encontrado = True
            if not encontrado:
                print("El título no está disponible en la biblioteca.")

    elif opcion == 5:
        agotados = False
        for i in range(len(titulos)):
            if ejemplares[i] == 0:
                print(f"{titulos[i]} está agotado.")
                agotados = True
        if not agotados:
            print("No hay títulos agotados.")

    elif opcion == 6:
        titulo_nuevo = input("Ingrese el nuevo título: ").strip()
        if titulo_nuevo == "":
            print("El título no puede estar vacío.")
        else:
            repetido = False
            for t in titulos:
                if t.lower() == titulo_nuevo.lower():
                    repetido = True
            if repetido:
                print("El título ya existe en la biblioteca.")
            else:
                while True:
                    try:
                        cant = int(input("Ingrese la cantidad de ejemplares: "))
                        if cant < 0:
                            print("La cantidad no puede ser negativa.")
                        else:
                            titulos.append(titulo_nuevo)
                            ejemplares.append(cant)
                            print("Título y ejemplares agregados con éxito.")
                            break
                    except ValueError:
                        print("Por favor, ingrese un número entero válido.")

    elif opcion == 7:
        if len(titulos) == 0:
            print("No hay títulos cargados.")
        else:
            consulta = input("Ingrese el título: ").strip()
            pos = -1
            for i in range(len(titulos)):
                if titulos[i].lower() == consulta.lower():
                    pos = i
            if pos == -1:
                print("El título no está disponible en la biblioteca.")
            else:
                accion = input("¿Desea realizar un préstamo (p) o devolución (d)?: ").strip().lower()
                if accion == "p":
                    while True:
                        try:
                            cant = int(input("Ingrese la cantidad a prestar: "))
                            if cant <= 0:
                                print("La cantidad debe ser positiva.")
                            elif cant > ejemplares[pos]:
                                print("No hay ejemplares suficientes disponibles.")
                            else:
                                ejemplares[pos] -= cant
                                print("Préstamo realizado con éxito.")
                                break
                        except ValueError:
                            print("Por favor, ingrese un número entero válido.")
                elif accion == "d":
                    while True:
                        try:
                            cant = int(input("Ingrese la cantidad a devolver: "))
                            if cant <= 0:
                                print("La cantidad debe ser positiva.")
                            else:
                                ejemplares[pos] += cant
                                print("Devolución realizada con éxito.")
                                break
                        except ValueError:
                            print("Por favor, ingrese un número entero válido.")
                else:
                    print("Opción inválida.")

    elif opcion == 8:
        salir = True
        print("Fin del programa.")

    else:
        print("Opción inválida.")
