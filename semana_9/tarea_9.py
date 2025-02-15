# Clase Producto: representa un producto en el inventario.
class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        :param producto_id: ID único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible del producto.
        :param precio: Precio unitario del producto..
        """
        self.producto_id = producto_id  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad de productos disponibles
        self.precio = precio  # Precio del producto

    # Métodos Getters y Setters
    def get_producto_id(self):
        return self.producto_id

    def set_producto_id(self, producto_id):
        self.producto_id = producto_id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

# Clase Inventario: maneja un conjunto de productos.
class Inventario:
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa una lista vacía de productos.
        """
        self.productos = []

    def añadir_producto(self, producto):
        """
        Añadir un nuevo producto al inventario si el ID es único.
        :param producto: Instancia de la clase Producto.
        :return: True si el producto fue añadido, False si el ID no es único.
        """
        # Verificar si el ID ya existe
        for p in self.productos:
            if p.get_producto_id() == producto.get_producto_id():
                return False  # El ID ya existe
        self.productos.append(producto)  # Añadir el producto
        return True

    def eliminar_producto(self, producto_id):
        """
        Eliminar un producto del inventario por su ID.
        :param producto_id: ID del producto a eliminar.
        :return: True si el producto fue eliminado, False si no se encontró.
        """
        for p in self.productos:
            if p.get_producto_id() == producto_id:
                self.productos.remove(p)  # Eliminar el producto
                return True
        return False  # No se encontró el producto

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        """
        Actualizar la cantidad o precio de un producto por su ID.
        :param producto_id: ID del producto a actualizar.
        :param cantidad: Nueva cantidad, si se desea actualizar.
        :param precio: Nuevo precio, si se desea actualizar.
        :return: True si se actualizó, False si no se encontró el producto.
        """
        for p in self.productos:
            if p.get_producto_id() == producto_id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                return True
        return False  # No se encontró el producto

    def buscar_producto(self, nombre):
        """
        Buscar productos por nombre (puede haber coincidencias parciales).
        :param nombre: Nombre o parte del nombre del producto.
        :return: Lista de productos que contienen el nombre buscado.
        """
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_productos(self):
        """
        Mostrar todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
            return
        for p in self.productos:
            print(f"ID: {p.get_producto_id()}, Nombre: {p.get_nombre()}, "
                  f"Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")

# Función para mostrar el menú interactivo en consola.
def mostrar_menu():
    print("\nMenú de Gestión de Inventario:")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto")
    print("5. Mostrar Todos los Productos")
    print("6. Salir")

# Función principal para gestionar la interacción con el usuario
def gestionar_inventario():
    inventario = Inventario()  # Creamos una instancia del inventario
    while True:
        mostrar_menu()  # Mostrar el menú de opciones
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            # para ñadir productos
            producto_id = int(input("Ingrese el ID del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(producto_id, nombre, cantidad, precio)

            if inventario.añadir_producto(producto):
                print("Producto añadido correctamente.")
            else:
                print("Error: El ID del producto ya existe.")

        elif opcion == '2':
            # permite eliminar los productos
            producto_id = int(input("Ingrese el ID del producto a eliminar: "))
            if inventario.eliminar_producto(producto_id):
                print("Producto eliminado correctamente.")
            else:
                print("Error: No se encontró el producto con ese ID.")

        elif opcion == '3':
            # codigo para actualizar los productos
            producto_id = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            if inventario.actualizar_producto(producto_id, cantidad, precio):
                print("Producto actualizado correctamente.")
            else:
                print("Error: No se encontró el producto con ese ID.")

        elif opcion == '4':
            # para buscar los productos
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for p in resultados:
                    print(f"ID: {p.get_producto_id()}, Nombre: {p.get_nombre()}, "
                          f"Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            # Muestra todos los productos
            inventario.mostrar_productos()

        elif opcion == '6':
            # codigo para salir
            print("Gracias por utilizar el sistema de gestión de inventarios.")
            break
        else:
            print("Opción no válida, por favor elija una opción entre 1 y 6.")

# Ejecuta la función principal
if __name__ == "__main__":
    gestionar_inventario()