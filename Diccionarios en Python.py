#Creación de Diccionario
informacion_personal = {"nombre": "Jimin", "edad": 24, "ciudad": "Paris", "profesión": "Policía"}
# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal ["ciudad"] = "Italia"
# Nueva clave-valor al diccionario que representa la "profesión" de la persona
informacion_personal ["profesión"] = "Bailarín"
# Verifica si la clave "telefono" existe y si no existe agregarla con un número de teléfono
if "teléfono" not in informacion_personal:
    informacion_personal["teléfono"] = "2456789100"
# Eliminar la clave "edad" del diccionario
del(informacion_personal["edad"])
# Imprimir el diccionario actualizado
print(informacion_personal)
