"AUXILIAR 2"
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
            especialidades.append(nueva_especialidad) # Ingreso efectivo
            cupos.append(0) # Se le añade 0 cupos a la especialidad recién añadida
    else:
        nueva_especialidad= print("La especialidad solo debe contener letras. ")
