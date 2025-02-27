import json

# representa un producto individual en el inventario
class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.producto_id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio


# gestiona el inventario utilizando un diccionario
class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.producto_id in self.productos:
            print(f"Producto con ID {producto.producto_id} ya existe.")
        else:
            self.productos[producto.producto_id] = producto
            print(f"Producto {producto.nombre} añadido exitosamente.")

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]
            print(f"Producto con ID {producto_id} eliminado exitosamente.")
        else:
            print(f"Producto con ID {producto_id} no encontrado.")

    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if nueva_cantidad is not None:
                producto.actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.actualizar_precio(nuevo_precio)
            print(f"Producto con ID {producto_id} actualizado exitosamente.")
        else:
            print(f"Producto con ID {producto_id} no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [prod for prod in self.productos.values() if nombre.lower() in prod.nombre.lower()]
        if resultados:
            for prod in resultados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for prod in self.productos.values():
                print(prod)

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as file:
            # Serializamos los productos a un formato JSON
            data = {id: prod.__dict__ for id, prod in self.productos.items()}
            json.dump(data, file)
            print("Inventario guardado exitosamente.")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as file:
                data = json.load(file)
                self.productos = {int(id): Producto(**prod) for id, prod in data.items()}
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("No se encontró el archivo, creando nuevo inventario.")
        except json.JSONDecodeError:
            print("Error al leer el archivo, formato incorrecto.")


# interfaz de usuario
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo('inventario.json')

    while True:
        print("\n-- Menú de Gestión de Inventario --")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")

        opcion = input("Seleccione una opción (1-8): ")

        if opcion == '1':
            producto_id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(producto_id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            producto_id = int(input("Ingrese el ID del producto a eliminar: "))
            inventario.eliminar_producto(producto_id)

        elif opcion == '3':
            producto_id = int(input("Ingrese el ID del producto a actualizar: "))
            nueva_cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            nuevo_precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(producto_id, nueva_cantidad, nuevo_precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            inventario.guardar_en_archivo('inventario.json')

        elif opcion == '7':
            inventario.cargar_desde_archivo('inventario.json')

        elif opcion == '8':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    menu()