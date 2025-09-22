"AUXILIAR"
#----------------------------------#

especialidades=["espe1","espe2","espe3"]
cupos=[10,11,12]

for i in range(len(especialidades)):
    if cupos[i] == 0:
        print(f"{especialidades[i]} no tiene cupos.")
    else:
        print("Todas las especialidades tienen cupos.")
        break






# espe_ver_cupos=input("Ingrese la especialidad: ")
# if espe_ver_cupos in especialidades:
#     indice_ver_cupos=especialidades.index(espe_ver_cupos)
#     print(f"Hay {cupos[indice_ver_cupos]} disponibles.")
# else:
#     print("La especialidad ingresada no está disponible.")
