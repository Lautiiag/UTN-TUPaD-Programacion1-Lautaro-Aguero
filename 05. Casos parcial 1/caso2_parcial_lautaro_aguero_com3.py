"CASO 2 PARCIAL 1: CLINICA"
# Respecto al documento: Opción 7 estaba repetida. Opción 6 se ve resuleta en opción 1.
# Opción 9 es redundante, se omite.


# Inicialización de listas y variables
especialidades=[]
cupos=[]

# Elegir opción
opciones=["1","2","3","4","5","6","7"]

salir=False
while salir == False:
    # Menú
    print("-----------MENÚ CLÍNICA-----------")
    print("1. Ingresar lista de especialidades")
    print("2. Ingresar lista de cupos disponibles por especialidad")
    print("3. Mostrar agenda")
    print("4. Consultar cupos de una especialidad")
    print("5. Listar especialidades sin cupo")
    print("6. Actualizar cupos (reservar/cancelar): ")
    print("7. Salir")

    opcion=(input("Ingrese una opción: ")) 
    while opcion not in opciones:
        opcion=(input("Ingrese una opción válida: "))

    match opcion:
        case "1":
            cant_especialidades=int(input("Ingrese cantidad de especialidades a añadir: "))
            for i in range(cant_especialidades):
                print(f"Ingrese especialidad {i+1}:")
                nueva_especialidad=input("Ingrese nueva especialidad: ").capitalize().strip()
                if nueva_especialidad.isalpha(): # Valida que la nueva especialidad no tenga números
                    if nueva_especialidad in especialidades: # Valida que la especialidad no esté en la lista
                        print("Esta especialidad ya fue añadida.")
                    else:
                        especialidades.append(nueva_especialidad) # Ingreso de especialidad efectiva
                        cupos_disponibles=input("Ingrese una cantidad de cupos disponibles: ")
                        if cupos_disponibles.isdigit(): # Valida que la cantidad de cupos sean números
                            cupos.append(cupos_disponibles) # Ingreso de cupos efectivo
                        else:
                            print("La cantidad de cupos ingresada no es válida.")
                            del especialidades[-1]
                else:
                    nueva_especialidad= print("La especialidad solo debe contener letras. ")

        case "2":
            for i in range(len(especialidades)):
                cant_cupos=(input(f"Ingrese cantidad de cupos para {especialidades[i]}: "))
                while not cant_cupos.isdigit(): # Valida que la cantidad sea números
                    cant_cupos=input(f"Ingrese una cantidad válida para {especialidades[i]}: ")
                    continue
                int(cant_cupos)
                cupos.append(cant_cupos)

        case "3":
            for i in range(len(especialidades)):
                print(f"{especialidades[i]} tiene {cupos[i]} cupo(s). ")

        case "4":
            espe_ver_cupos=input("Ingrese la especialidad: ").capitalize().strip()
            if espe_ver_cupos in especialidades:
                indice_ver_cupos=especialidades.index(espe_ver_cupos)
                print(f"Hay {cupos[indice_ver_cupos]} disponibles.")
            else:
                print("La especialidad ingresada no está disponible.")

        case "5":
            for i in range(len(especialidades)):
                if cupos[i] == 0:
                    print(f"{especialidades[i]} no tiene cupos.")
                else:
                    print("Todas las especialidades tienen cupos.")
                    break
        case "6":
            espe_cambiar_cupo=input("Ingrese el nombre de la especialidad: ").capitalize().strip()
            if espe_cambiar_cupo in especialidades:
                nueva_cant_cupos=input("Ingrese nueva cantidad de cupos: ")
                if nueva_cant_cupos.isdigit():
                    cupos[especialidades.index(espe_cambiar_cupo)]=int(nueva_cant_cupos)
                else:
                    print("Ingrese una cantidad de cupos válida. ")
            else:
                print("La especialidad no se encuentra añadida.")

        case "7":
            salir=True
