class Libro:
    """Representa un libro en la biblioteca."""
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False

    def prestar(self):
        """Presta el libro si no está prestado."""
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        """Devuelve el libro."""
        self.prestado = False
        print(f"El libro '{self.titulo}' ha sido devuelto.")

class Usuario:
    """Representa un usuario de la biblioteca."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def pedir_prestado(self, libro):
        """Permite al usuario pedir prestado un libro."""
        if not libro.prestado:
            libro.prestar()
            self.libros_prestados.append(libro)
        else:
            print(f"{self.nombre} no puede pedir prestado el libro '{libro.titulo}'.")

# uso del sistema de biblioteca
libro1 = Libro("El principito", "Antoine de Saint-Exupéry", "123456")
usuario1 = Usuario("María")

usuario1.pedir_prestado(libro1)  # María pide prestado el libro
libro1.devolver()  # El libro es devuelto