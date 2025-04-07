import tkinter as tk
from tkinter import messagebox

class GestorDeTareas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestor de Tareas Pendientes")
        self.ventana.geometry("500x400")
        self.ventana.config(bg="#f0f0f0")  # Fondo gris claro

        self.tareas = []  # Lista que almacena las tareas

        # Crear los widgets de la interfaz
        self.configurar_widgets()

        # Asociar atajos de teclado a funciones
        self.ventana.bind("<Return>", self.agregar_tarea_por_teclado)
        self.ventana.bind("<c>", self.marcar_tarea_completada)
        self.ventana.bind("<Delete>", self.eliminar_tarea)
        self.ventana.bind("<Escape>", self.salir)

    def configurar_widgets(self):
        # Campo de entrada para agregar nuevas tareas
        self.entrada_tarea = tk.Entry(self.ventana, width=35, font=("Arial", 14))
        self.entrada_tarea.grid(row=0, column=0, padx=10, pady=10, columnspan=2)  # Ajustado con grid

        # Botón para agregar una tarea
        self.boton_agregar = tk.Button(self.ventana, text="Agregar Tarea", width=20, height=2,
                                       font=("Arial", 12), bg="#4CAF50", fg="white", command=self.agregar_tarea)
        self.boton_agregar.grid(row=1, column=0, padx=10, pady=5)

        # Botón para marcar tarea como completada
        self.boton_completar = tk.Button(self.ventana, text="Completar Tarea", width=20, height=2,
                                         font=("Arial", 12), bg="#FF9800", fg="white", command=self.marcar_tarea_completada)
        self.boton_completar.grid(row=1, column=1, padx=10, pady=5)

        # Lista de tareas
        self.lista_tareas = tk.Listbox(self.ventana, height=10, width=45, selectmode=tk.SINGLE, font=("Arial", 12))
        self.lista_tareas.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Botón para eliminar tarea
        self.boton_eliminar = tk.Button(self.ventana, text="Eliminar Tarea", width=20, height=2,
                                        font=("Arial", 12), bg="#f44336", fg="white", command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=3, column=0, padx=10, pady=5)

        # Botón para cerrar la aplicación
        self.boton_salir = tk.Button(self.ventana, text="Salir", width=20, height=2,
                                     font=("Arial", 12), bg="#607D8B", fg="white", command=self.salir)
        self.boton_salir.grid(row=3, column=1, padx=10, pady=5)

    # Función para agregar tarea desde el botón
    def agregar_tarea(self):
        tarea = self.entrada_tarea.get()  # Obtener el texto de la tarea
        if tarea:
            self.tareas.append({"tarea": tarea, "completada": False})  # Agregar tarea a la lista
            self.actualizar_lista_tareas()  # Actualizar la visualización
            self.entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Campo vacío", "Por favor, ingresa una tarea.")

    # Función para agregar tarea presionando "Enter"
    def agregar_tarea_por_teclado(self, evento):
        self.agregar_tarea()  # Llamar a la función que agrega la tarea

    # Función para marcar tarea como completada
    def marcar_tarea_completada(self, evento=None):
        tarea_seleccionada = self.lista_tareas.curselection()  # Obtener tarea seleccionada
        if tarea_seleccionada:
            indice = tarea_seleccionada[0]  # Obtener índice de la tarea seleccionada
            self.tareas[indice]["completada"] = True  # Marcar como completada
            self.actualizar_lista_tareas()  # Actualizar lista de tareas
        else:
            messagebox.showwarning("Selección necesaria", "Selecciona una tarea para marcar como completada.")

    # Función para eliminar tarea seleccionada
    def eliminar_tarea(self, evento=None):
        tarea_seleccionada = self.lista_tareas.curselection()  # Obtener tarea seleccionada
        if tarea_seleccionada:
            indice = tarea_seleccionada[0]  # Obtener índice de la tarea seleccionada
            del self.tareas[indice]  # Eliminar tarea de la lista
            self.actualizar_lista_tareas()  # Actualizar lista de tareas
        else:
            messagebox.showwarning("Selección necesaria", "Selecciona una tarea para eliminarla.")

    # Función para actualizar la lista de tareas visualmente
    def actualizar_lista_tareas(self):
        self.lista_tareas.delete(0, tk.END)  # Limpiar la lista de tareas
        for tarea in self.tareas:
            if tarea["completada"]:
                self.lista_tareas.insert(tk.END, f"{tarea['tarea']} - Completada")  # Mostrar tarea completada
            else:
                self.lista_tareas.insert(tk.END, tarea["tarea"])  # Mostrar tarea pendiente

    # Función para salir de la aplicación
    def salir(self, evento=None):
        self.ventana.quit()  # Cerrar la ventana y la aplicación

# Código principal para ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()  # Crear la ventana principal
    aplicacion = GestorDeTareas(ventana)  # Crear una instancia de la clase GestorDeTareas
    ventana.mainloop()  # Iniciar el bucle de la interfaz gráfica.