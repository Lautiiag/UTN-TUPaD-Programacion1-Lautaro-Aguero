"PRUEBAS"
hemisferio=input("En qué hemisferio se encuentra (N/S)?").lower()
mes=int(input("En qué número de mes se encuentra?"))
dia=int(input("Que dia es?"))

if hemisferio == "s" :
    if mes in (12,1,2,3):
        print("Actualmente se encuentra en Verano.")
