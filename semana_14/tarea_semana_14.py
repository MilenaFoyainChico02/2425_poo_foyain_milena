import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.simpledialog


# Función para agregar un evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        # Agregar el evento a la lista (TreeView)
        tree.insert("", "end", values=(fecha, hora, descripcion))
        # Limpiar campos de entrada
        entry_fecha.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada incompleta", "Por favor, complete todos los campos.")


# Función para eliminar un evento seleccionado
def eliminar_evento():
    # Obtener el ítem seleccionado en el TreeView
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showwarning("Sin selección", "Por favor, selecciona un evento para eliminar.")
        return

    # Confirmación antes de eliminar
    respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar este evento?")
    if respuesta:
        tree.delete(selected_item)


# Función para salir de la aplicación
def salir():
    root.quit()


# Crea la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("600x400")

# Crear un frame para la lista de eventos
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

# TreeView para mostrar los eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Crea un frame para los campos de entrada
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Etiquetas y campos de entrada para fecha, hora y descripción
label_fecha = tk.Label(frame_entrada, text="Fecha (DD/MM/YYYY):")
label_fecha.grid(row=0, column=0, padx=5, pady=5)
entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

label_hora = tk.Label(frame_entrada, text="Hora (HH:MM):")
label_hora.grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Crea un frame para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botones para agregar, eliminar eventos y salir
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5, pady=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=5, pady=5)

# Inicia la gestión de la aplicación
root.mainloop()