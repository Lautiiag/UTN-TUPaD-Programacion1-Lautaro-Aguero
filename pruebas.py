"PRUEBAS"
#----------------------------------#

frase=input("Ingrese una frase o palabra: ").lower().strip()
vocal=("a","e","i","o","u")
if frase.endswith(vocal):
    print(frase + "!")
else:
    print(frase)