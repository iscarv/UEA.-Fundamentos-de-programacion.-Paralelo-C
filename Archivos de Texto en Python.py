# 1. Escritura de Archivo de Texto:
with open("my_notes.txt", "w") as archivo:
# Escribe al menos tres líneas de notas personales en el archivo.
     archivo.write("Notas personales:\n")
     archivo.write("1. Terminar el proyecto de ciencias naturales.\n")
     archivo.write("2. Arreglar mi cuarto.\n")
     archivo.write("3. Correguir la tarea de lenguaje.\n")

# 2. Lectura de Archivo de Texto:
archivo = open("my_notes.txt", "r")
# Leer e imprimir cada línea del archivo
linea = archivo.readline()  # Leer la primera línea
while linea:
    print(linea.strip())  # Mostrar en la consola cada línea leída
    linea = archivo.readline()  # Leer la siguiente línea
# 3. Cerrar el archivo después de realizar las operaciones necesarias
archivo.close()