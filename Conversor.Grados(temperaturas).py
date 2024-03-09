#Función para convertir grados centigrados a Fahrenheit, a grados Kelvin
def celsius_a_fahrenheit(grad_cent):
    """Convierte grados Celsius a fahrenheit."""
    fahrenheit = (9/5)*(grad_cent)+32
    return fahrenheit
def celsius_a_kelvin(grad_cent):
    """Convierte grados Celsius a grados kelvin."""
    kelvin = 273.15 + grad_cent
    return kelvin
grad_cent = float(input("Ingrese la temperatura en grados Celsius: "))
print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(grad_cent))
print("Temperatura en Kelvin:", celsius_a_kelvin(grad_cent))
