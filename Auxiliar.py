"AUXILIAR"
#----------------------------------#
especialidades=["espe1","espe2","espe3","espe4"]
cupos=[1,2,3,4]


espe_cambiar_cupo=input("Ingrese el nombre de la especialidad: ")
if espe_cambiar_cupo in especialidades:
    nueva_cant_cupos=input("Ingrese nueva cantidad de cupos: ")
    if nueva_cant_cupos.isdigit():
        cupos[especialidades.index(espe_cambiar_cupo)]=int(nueva_cant_cupos)
    else:
        print("Ingrese una cantidad de cupos válida. ")
else:
    print("La especialidad no se encuentra añadida.")

print(especialidades)
print(cupos)
