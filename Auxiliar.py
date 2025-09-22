"AUXILIAR"
#----------------------------------#

especialidades=[]
cupos=[]

cant_especialidades=int(input("Ingrese cantidad de especialidades a añadir: "))
for i in range(cant_especialidades):
    nueva_especialidad=input("Ingrese nueva especialidad: ").capitalize()
    if nueva_especialidad.isalpha(): # Valida que sea string
        especialidades.append(nueva_especialidad)
    else:
        while nueva_especialidad :
            nueva_especialidad= input("Ingrese una especialidad válida: ")
    print(especialidades)
