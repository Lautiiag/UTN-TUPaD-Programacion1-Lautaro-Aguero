"AUXILIAR"
#----------------------------------#
especialidades=[]
cupos=[]


cant_especialidades=int(input("Ingrese cantidad de especialidades a añadir: "))
for i in range(cant_especialidades):
    print(f"Ingrese especialidad {i+1}:")
    nueva_especialidad=input("Ingrese nueva especialidad: ").capitalize()
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
    print(especialidades)
    print(cupos)
