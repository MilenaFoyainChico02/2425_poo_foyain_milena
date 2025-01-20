# Clase base
class Vehiculo:
    def __init__(self, marca, modelo, tipo_motor, precio):
        self.marca = marca  # Marca del vehículo
        self.modelo = modelo  # Modelo del vehículo
        self.tipo_motor = tipo_motor  # Tipo de motor
        self.__precio = precio  # Precio del vehículo (privado)

    # Método para mostrar la información del vehículo
    def mostrar_informacion(self):
        return f"Vehículo: {self.marca} {self.modelo}, Motor: {self.tipo_motor}."

    # Métodos para manejar el precio (encapsulación)
    def obtener_precio(self):
        return self.__precio

    def establecer_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser un valor positivo.")

# Clase derivada
class Auto(Vehiculo):
    def __init__(self, marca, modelo, tipo_motor, precio, cantidad_puertas, capacidad_baul):
        super().__init__(marca, modelo, tipo_motor, precio)
        self.cantidad_puertas = cantidad_puertas  # Cantidad de puertas
        self.capacidad_baul = capacidad_baul  # Capacidad del baúl en litros

    # Sobrescribir el método mostrar_informacion
    def mostrar_informacion(self):
        informacion_base = super().mostrar_informacion()
        return f"{informacion_base} Puertas: {self.cantidad_puertas}, Baúl: {self.capacidad_baul}L."

# Clase derivada
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo_motor, precio, cilindrada, tipo_moto):
        super().__init__(marca, modelo, tipo_motor, precio)
        self.cilindrada = cilindrada  # Cilindrada del motor
        self.tipo_moto = tipo_moto  # Tipo de motocicleta (ej. deportiva, turismo)

    # Sobrescribir el método mostrar_informacion
    def mostrar_informacion(self):
        informacion_base = super().mostrar_informacion()
        return f"{informacion_base} Cilindrada: {self.cilindrada}cc, Tipo: {self.tipo_moto}."



# Crear instancias de Auto y Moto
auto1 = Auto("Toyota", "Corolla", "Híbrido", 25000, 4, 470)
moto1 = Moto("Yamaha", "MT-07", "Gasolina", 7500, 689, "Deportiva")

# Mostrar información de los vehículos
print(auto1.mostrar_informacion())
print(f"Precio: ${auto1.obtener_precio()}")

print(moto1.mostrar_informacion())
print(f"Precio: ${moto1.obtener_precio()}")

# Actualizar precios
auto1.establecer_precio(26000)
moto1.establecer_precio(8000)

print(f"Nuevo precio del {auto1.modelo}: ${auto1.obtener_precio()}")
print(f"Nuevo precio de la {moto1.modelo}: ${moto1.obtener_precio()}")