"AUXILIAR 2"
#----------------------------------#

especialidades=[]
cupos=[]

cant_especialidades=int(input("Ingrese cantidad de especialidades a añadir: "))
for i in range(cant_especialidades):
    nueva_especialidad=input("Ingrese nueva especialidad: ").capitalize()
    if nueva_especialidad is str: # Valida que sea string
        if nueva_especialidad in especialidades: #Valida se está añadida
            print("Esta especialidad ya fue añadida.")
        else:
            especialidades.append(nueva_especialidad)
    else:
        while nueva_especialidad is not str:
            nueva_especialidad= input("Ingrese una especialidad válida: ")
    print(especialidades)
