#Desarrollo de Función para Calcular Temperaturas Promedio
# Calcular el promedio de temperaturas para múltiples ciudades y semanas.
#Uso de la Función
def temperatura_promedio(ciudades_temperaturas):
    temperaturas_promedio= {}
    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas)/len(temperaturas)
        temperaturas_promedio[ciudad] = promedio
    return temperaturas_promedio
#Lista de ciudades con variables de temperaturas
ciudades_temperaturas = {
    "Esmeraldas": [75, 90, 81, 76, 77, 78, 92],  #Una semana de temperaturas de la ciudad de Esmeraldas
    "Quito" : [80, 81, 93, 74, 85, 75, 91], #Una semana de temperaturas de la ciudad de Quito
    "Guayaquil": [73, 81, 80, 83, 96, 89, 94], #Una semana de temperaturas de la ciudad de Guayaquil.
    "Manta" : [62, 74, 66, 68, 69, 80, 71], #Una semana de temperaturas de la ciudad de Manta.
    "Puyo": [85, 87, 89, 90, 92, 94, 82] #Una semana de temperaturas de la ciudad de Puyo.
    }
#Calculo del promedio de temperaturas por cada ciudad
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")


