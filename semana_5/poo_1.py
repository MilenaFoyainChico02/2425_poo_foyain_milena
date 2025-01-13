class ConversorLongitud:
    """Representa un conversor de metros a centímetros."""

    def __init__(self, metros):
        """Inicializa la longitud en metros."""
        self.metros = metros

    def convertir_a_centimetros(self):
        """Convierte la longitud de metros a centímetros y devuelve el resultado."""
        centimetros = self.metros * 100  # 1 metro = 100 centímetros
        return centimetros

    def mostrar_resultado(self):
        """Muestra el resultado de la conversión de manera formateada."""
        print(f"{self.metros} metros son {self.convertir_a_centimetros()} centímetros.")


# Ejemplo de uso del conversor de metros a centímetros
longitud1 = ConversorLongitud(2.5)  # Se crea una instancia con 2.5 metros
longitud1.mostrar_resultado()  # Muestra el resultado de la conversión