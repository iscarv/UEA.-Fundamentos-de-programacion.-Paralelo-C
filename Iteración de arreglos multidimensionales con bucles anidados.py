#Iteración de arreglos multidimensionales con bucles anidados
# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 81},
            {"day": "Jueves", "temp": 76},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 92}],

        [   # Semana 2
            {"day": "Lunes", "temp": 80},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 74},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 91}],

        [   # Semana 3
            {"day": "Lunes", "temp": 73},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 83},
            {"day": "Viernes", "temp": 96},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 94}],

        [   # Semana 4
            {"day": "Lunes", "temp": 70},
            {"day": "Martes", "temp": 72},
            {"day": "Miércoles", "temp": 81},
            {"day": "Jueves", "temp": 85},
            {"day": "Viernes", "temp": 93},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 92}]],

    [ # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 74},
            {"day": "Miércoles", "temp": 66},
            {"day": "Jueves", "temp": 68},
            {"day": "Viernes", "temp": 69},
            {"day": "Sábado", "temp": 80},
            {"day": "Domingo", "temp": 71}],

        [   # Semana 2
            {"day": "Lunes", "temp": 70},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 60},
            {"day": "Jueves", "temp": 61},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 79},
            {"day": "Domingo", "temp": 82}],

        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 63},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 77},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 80}],

        [   # Semana 4
            {"day": "Lunes", "temp": 60},
            {"day": "Martes", "temp": 85},
            {"day": "Miércoles", "temp": 87},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 65},
            {"day": "Domingo", "temp": 69}]],
    [ # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 92},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 97},
            {"day": "Jueves", "temp": 83},
            {"day": "Viernes", "temp": 93},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 90}],

        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}],

        [   # Semana 3
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 86},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 82},
            {"day": "Domingo", "temp": 80}],

        [   # Semana 4
            {"day": "Lunes", "temp": 85},
            {"day": "Martes", "temp": 87},
            {"day": "Miércoles", "temp": 89},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 92},
            {"day": "Sábado", "temp": 94},
            {"day": "Domingo", "temp": 82}]]
]
# Calcular el promedio de temperaturas para cada ciudad y semana
for i in range(len(temperaturas)):
    print(f"Promedio de temperaturas para la Ciudad {i + 1}:")
    for j in range(len(temperaturas[i])):
        suma = sum(dia['temp'] for dia in temperaturas[i][j])
        promedio = suma / len(temperaturas[i][j])
        print(f"Semana {j + 1}: {promedio}")
        print()  # Salto de línea para separar las ciudades




