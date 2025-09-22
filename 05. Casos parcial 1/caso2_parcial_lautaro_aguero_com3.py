"CASO 2 PARCIAL 1: CLINICA"

# Inicialización de listas y variables
especialidades=[]
cupos=[]

# Menú
print("MENÚ CLÍNICA")
print("1. Ingresar lista de especialidades")
print("2. Ingresar lista de cupos disponibles por especialidad")
print("3. Mostrar agenda")
print("4. Consultar cupos de una especialidad")
print("5. Listar especialidades sin cupo")
print("6. Ver sin cupo")
print("7. Actualizar cupos (reservar/cancelar): ")
print("8. Ver agenda: ")
print("9. Salir")

# Elegir opción
opciones=["1","2","3","4","5","6","7","8","9"]

salir=False
while salir == False:

    opcion=(input("Ingrese una opción: ")) 
    while opcion not in opciones:
        opcion=(input("Ingrese una opción válida: "))

    match opcion:
        case "1":
            cant_especialidades=int(input("Ingrese cantidad de especialidades a añadir: "))
            for i in range(cant_especialidades):
                print(f"Ingrese especialidad {i+1}:")
                nueva_especialidad=input("Ingrese nueva especialidad: ").capitalize()
                if nueva_especialidad.isalpha(): # Valida que la nueva especialidad no tenga números
                    if nueva_especialidad in especialidades: # Valida que la especialidad no esté en la lista
                        print("Esta especialidad ya fue añadida.")
                    else:
                        especialidades.append(nueva_especialidad)
                else:
                    nueva_especialidad= print("La especialidad solo debe contener letras. ")

        case "2":
            for i in range(len(especialidades)):
                cant_cupos=(input(f"Ingrese cantidad de cupos para {especialidades[i]}: "))
                while not cant_cupos.isdigit(): # Valida que la cantidad sea números
                    cant_cupos=input(f"Ingrese una cantidad válida para {especialidades[i]}: ")
                    continue
                cupos.append(cant_cupos)

        case "3":
            for i in range(len(especialidades)):
                print(f"{especialidades[i]} tiene {cupos[i]} cupos. ")

        case "4":
            especialidades=["espe1","espe2","espe3"]
            cupos=[10,11,12]
            
            espe_ver_cupos=input("Ingrese la especialidad: ")
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
            print("Ingreso 6")
        case "7":
            print("Ingreso 7")
        case "8":
            print("Ingreso 8")
        case "9":
            salir=True
