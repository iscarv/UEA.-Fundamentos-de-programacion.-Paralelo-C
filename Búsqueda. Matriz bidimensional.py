#Matriz Bidimensional
# Declaración de la variable bidimensional con enteros
variable_3x3 = [
               [1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]

#Búsqueda de un valor específico en la matriz
valor_buscado = 8

#Inicializar variables para rastrear la posición del valor
fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(variable_3x3)):
    for columna in range(len(variable_3x3[fila])):
        if variable_3x3 [fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break # Detener la búsqueda una vez que se encuentra el valor
    if fila_encontrada != -1:
        break # Salir del bucle si se encuentra el valor
# Verificar si se encontró el valor
if fila_encontrada != -1:
    print(f"Se encontró el número {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}")
else:
    print(f"El número {valor_buscado} no se encontró en la matriz")
