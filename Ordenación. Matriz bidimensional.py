#Matriz Bidimensional
# Declaración de la variable bidimensional con enteros
variable_3x3 = [
               [8, 2, 1],
               [3, 5, 4],
               [6, 7, 9]]
# Mostrar la matriz original
print("Matriz original:")
for fila in variable_3x3:
    print(fila)
# Ordenar la fila específica (en este caso, la primera fila)
fila_a_ordenar = 1  # Índice de la fila a ordenar
fila = variable_3x3[fila_a_ordenar]
n = len(fila)

# Algoritmo de ordenación de burbuja
for i in range(n-1):
    for j in range(0, n-i-1):
        if fila[j] > fila[j+1]:
            fila[j], fila[j+1] = fila[j+1], fila[j]

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for i in range(len(variable_3x3)):
    if i == fila_a_ordenar:
        print(fila)  # Mostrar la fila ordenada
    else:
        print(variable_3x3[i])  # Mantener las otras filas sin cambios