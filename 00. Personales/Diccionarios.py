"Diccionarios"
# Crear Diccionario
persona = {
"nombre": "Lucía",
"edad": 28,
"profesion": "Diseñadora"
}

# Imprir: Lucía
print(persona["nombre"]) 
# Agregar o modificar
persona["edad"] = 29
# Eliminar
del persona["profesion"]
# Ver todas las claves
print(persona.keys())
# Ver todos los valores
print(persona.values())
# Recorrer con for
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
