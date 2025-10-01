"Ahorcado temática de vegetales y frutas"
import random


def eleccion_de_palabra(palabras):
    palabra_elegida=palabras[random.randrange(0,len(palabras))]
    return palabra_elegida

def print_guiones(palabra_elegida):
    for i in range(len(palabra_elegida)):
        print("_", end=" ")






palabras=("pera", "banana", "manzana", "naranja", "mandarina", "uva", "zapallo", "papa", "apio", "pepino", "durazno")
palabra_elegida=eleccion_de_palabra(palabras)
print(palabra_elegida)

