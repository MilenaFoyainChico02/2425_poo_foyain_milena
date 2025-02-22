import os
import json
# Clase Producto: representa un producto en el inventario.
class Producto:
    def _init_(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {
            "producto_id": self.producto_id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data["producto_id"], data["nombre"], data["cantidad"], data["precio"])


# Clase Inventario con almacenamiento en archivo
class Inventario:
    ARCHIVO = "inventario.txt"

    def _init_(self):
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO, "w") as file:
                json.dump([p.to_dict() for p in self.productos], file)
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el archivo: {e}")

    def cargar_desde_archivo(self):
        if not os.path.exists(self.ARCHIVO):
            return
        try:
            with open(self.ARCHIVO, "r") as file:
                self.productos = [Producto.from_dict(p) for p in json.load(file)]
        except (FileNotFoundError, PermissionError, json.JSONDecodeError) as e:
            print(f"Error al leer el archivo: {e}")

    def añadir_producto(self, producto):
        if any(p.producto_id == producto.producto_id for p in self.productos):
            return False
        self.productos.append(producto)
        self.guardar_en_archivo()
        return True

    def eliminar_producto(self, producto_id):
        for p in self.productos:
            if p.producto_id == producto_id:
                self.productos.remove(p)
                self.guardar_en_archivo()
                return True
        return False

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        for p in self.productos:
            if p.producto_id == producto_id:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                self.guardar_en_archivo()
                return True
        return False

    def buscar_producto(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos:
            print(f"ID: {p.producto_id}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")


# Función para mostrar el menú en consola
def mostrar_menu():
    print("\nMenú de Gestión de Inventario:")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto")
    print("5. Mostrar Todos los Productos")
    print("6. Salir")


# Función principal
def gestionar_inventario():
    inventario = Inventario()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        if opcion == '1':
            try:
                producto_id = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                producto = Producto(producto_id, nombre, cantidad, precio)
                if inventario.añadir_producto(producto):
                    print("Producto añadido correctamente.")
                else:
                    print("Error: El ID del producto ya existe.")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para ID, cantidad y precio.")
        elif opcion == '2':
            try:
                producto_id = int(input("Ingrese el ID del producto a eliminar: "))
                if inventario.eliminar_producto(producto_id):
                    print("Producto eliminado correctamente.")
                else:
                    print("Error: No se encontró el producto.")
            except ValueError:
                print("Error: Ingrese un ID válido.")
        elif opcion == '3':
            try:
                producto_id = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiarla): ")
                precio = input("Ingrese el nuevo precio (deje en blanco para no cambiarlo): ")
                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None
                if inventario.actualizar_producto(producto_id, cantidad, precio):
                    print("Producto actualizado correctamente.")
                else:
                    print("Error: No se encontró el producto.")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for p in resultados:
                    print(f"ID: {p.producto_id}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
            else:
                print("No se encontraron productos con ese nombre.")
        elif opcion == '5':
            inventario.mostrar_productos()
        elif opcion == '6':
            print("Gracias por usar el sistema de inventarios.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecuta el programa
if __name__ == "__main__":
    gestionar_inventario()