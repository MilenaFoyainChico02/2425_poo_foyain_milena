# inventario de una tienda sde ropa
class Producto:
    def __init__(self, nombre, precio, cantidad):
        """Constructor: Inicializa el producto con nombre, precio y cantidad."""
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"Producto '{self.nombre}' creado con precio: {self.precio} y cantidad: {self.cantidad}")

    def vender(self, cantidad_vendida):
        """Método para vender una cantidad de productos."""
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            print(f"Se han vendido {cantidad_vendida} unidades de '{self.nombre}'.")
        else:
            print(f"No hay suficiente stock de '{self.nombre}' para vender {cantidad_vendida} unidades.")

    def mostrar_informacion(self):
        """Método para mostrar la información del producto."""
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad disponible: {self.cantidad}")

    def __del__(self):
        """Destructor: Este método se llama cuando el objeto es destruido."""
        print(f"Destructor: El producto '{self.nombre}' ha sido eliminado del inventario.")


class Inventario:
    def __init__(self):
        """Constructor: Inicializa el inventario con una lista vacía."""
        self.productos = []
        print("Inventario creado. ¡Bienvenido a la tienda!")

    def agregar_producto(self, producto):
        """Método para agregar productos al inventario."""
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado al inventario.")

    def eliminar_producto(self, producto):
        """Método para eliminar un producto del inventario."""
        if producto in self.productos:
            self.productos.remove(producto)
            del producto  # Llamamos al destructor del producto
            print(f"Producto '{producto.nombre}' eliminado del inventario.")
        else:
            print(f"El producto '{producto.nombre}' no se encuentra en el inventario.")

    def mostrar_inventario(self):
        """Método para mostrar todos los productos en el inventario."""
        print("\nInventario de la tienda:")
        for producto in self.productos:
            producto.mostrar_informacion()

    def __del__(self):
        """Destructor: Se llama cuando el inventario es destruido."""
        print("Destructor: El inventario está siendo destruido.")
        for producto in self.productos:
            del producto  # Llamamos al destructor de cada producto


# Creación de productos
producto1 = Producto("Camiseta", 20, 50)
producto2 = Producto("Pantalón", 40, 30)
producto3 = Producto("Zapatos", 60, 20)

# Crea inventario y agrega productos
inventario = Inventario()
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)

# Muestra la información del inventario
inventario.mostrar_inventario()

# Venta de productos
producto1.vender(5)  # Venda de 5 camisetas
producto2.vender(10)  # Venda de 10 pantalones

# Muestra el inventario después de las ventas
inventario.mostrar_inventario()

# final del inventario
del inventario