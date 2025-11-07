mochila_bien_armada=False
while mochila_bien_armada == False:
    try:
        espacios_para_agregar=int(input("Ingrese la cantidad de espacio de la mochila: "))
        mochila_bien_armada=True
    except:
        print("No ingresó un número válido.")
