# Clase que representa la información de un día en términos de temperatura
class DiaClima:
    def __init__(self, temperatura):
        # Encapsulamos la temperatura, ya que es una propiedad privada
        self.__temperatura = temperatura

    # Método getter para obtener la temperatura
    def obtener_temperatura(self):
        return self.__temperatura

    # Método setter para modificar la temperatura si es necesario
    def establecer_temperatura(self, nueva_temperatura):
        if isinstance(nueva_temperatura, (int, float)):
            self.__temperatura = nueva_temperatura
        else:
            raise ValueError("La temperatura debe ser un número")


# Clase que representa la gestión de la semana de clima
class SemanaClima:
    def __init__(self):
        # lista para almacenar los días de la semana
        self.dias = []

    # Método para agregar un día de clima
    def agregar_dia(self, dia_clima):
        if len(self.dias) < 7:  # Limitamos a 7 días
            self.dias.append(dia_clima)
        else:
            raise ValueError("No se pueden agregar más de 7 días a la semana")

    # Método para calcular el promedio de la temperatura semanal
    def calcular_promedio_semanal(self):
        if len(self.dias) == 0:
            raise ValueError("No hay datos de temperatura para calcular el promedio")

        # Suma las temperaturas de todos los días de la semana
        total_temperaturas = sum(dia.obtener_temperatura() for dia in self.dias)
        # Calcula el promedio dividiendo entre el número de días
        promedio = total_temperaturas / len(self.dias)
        return promedio


# las temperaturas de cada día de la semana
lunes = DiaClima(32)
martes = DiaClima(33)
miercoles = DiaClima(25)
jueves = DiaClima(19)
viernes = DiaClima(41)
sabado = DiaClima(24)
domingo = DiaClima(29)

# Crea el objeto de SemanaClima
semana = SemanaClima()
# días a la semana
semana.agregar_dia(lunes)
semana.agregar_dia(martes)
semana.agregar_dia(miercoles)
semana.agregar_dia(jueves)
semana.agregar_dia(viernes)
semana.agregar_dia(sabado)
semana.agregar_dia(domingo)

# Calcula y mostretra el promedio semanal
promedio = semana.calcular_promedio_semanal()
print(f"El promedio de temperaturas de la semana es: {promedio:.2f}°C")

# la programación orientada a objetos (POO) organiza el código en clases y  objetos, facilitando la reutilización y el manejo de proyectos grandes
# la programación tradicional se basa en funciones y es más simple, ideal para proyectos pequeños o simples
# la POO es más compleja pero más escalable, mientras que la programación tradicional es más fácil de aprender y usar.