# programación tradicional
def registrar_temperaturas():
    """
    Esta función solicita al usuario que ingrese las temperaturas de cada día de la semana.
    Devuelve una lista con las temperaturas para los 7 días.
    """
    # lista vacia para almacenar las temperaturas
    temperaturas = []
    # usamos un bucle y establesemos un rango de dias
    for i in range(7):
        while True: # se repite el bucle hasta que que el valor que se ingrese sea valido
            try:
                # se pide ingresar las temperaturas
                temp = float(input(f"Introduce la temperatura del día {i+1}: "))
                # se agrega la temperatura ingresada a la lista
                temperaturas.append(temp)
                break # sale del bucle
            except ValueError: # si ocurre un error pedira que ingrese nuevamente la temperatura
                print("Por favor, ingresa un número válido.")
    return temperaturas

def obtener_promedio_semanal(temperaturas):
    """
    Esta función recibe una lista de temperaturas y calcula el promedio de la semana.
    Retorna el valor del promedio.
    """
    if len(temperaturas) == 7:  # verifica que hay 7 días de temperatura.
        # calcula el promedio de todas las temperaturas ingresadas
        promedio = sum(temperaturas) / len(temperaturas)
        return promedio
    # muestra error si los datos ingresados estan incompletos
    else:
        print("La lista de temperaturas debe tener exactamente 7 elementos.")
        return None

temperaturas = registrar_temperaturas()  # registra las temperaturas
promedio = obtener_promedio_semanal(temperaturas)  # calcula el promedio

if promedio is not None:
    print(f"La temperatura promedio de la semana es: {promedio:.2f}°C")


