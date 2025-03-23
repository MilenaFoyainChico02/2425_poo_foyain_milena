import tkinter as tk
from tkinter import ttk

# Función para agregar un elemento a la tabla
def agregar_elemento():
    dato = entrada_texto.get()
    if dato:
        tabla.insert("", "end", values=(dato,))
        entrada_texto.delete(0, tk.END)  # Limpiar solo el campo de texto después de agregar

# Función para limpiar la entrada de texto y la tabla
def limpiar_datos():
    entrada_texto.delete(0, tk.END)  # Limpia el campo de texto
    for item in tabla.get_children():
        tabla.delete(item)  # Borra todos los datos de la tabla

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Mejorada")
ventana.geometry("400x350")
ventana.configure(bg="#e6f7ff")  # Color de fondo de la ventana

# Etiqueta y campo de texto para ingresar datos
etiqueta = tk.Label(ventana, text="Ingrese un dato:", bg="#e6f7ff", font=("Arial", 10, "bold"))
etiqueta.pack(pady=5)

entrada_texto = tk.Entry(ventana, font=("Arial", 10))
entrada_texto.pack(pady=5)

# Frame para los botones
frame_botones = tk.Frame(ventana, bg="#e6f7ff")
frame_botones.pack(pady=5)

# Botón para agregar datos
boton_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_elemento,
                           bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
                           width=12, height=1)
boton_agregar.pack(pady=2)  # Espaciado entre botones

# Botón para limpiar la entrada y la tabla (debajo del de agregar)
boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_datos,
                          bg="#f44336", fg="white", font=("Arial", 10, "bold"),
                          width=12, height=1)
boton_limpiar.pack(pady=2)  # Espaciado entre botones

# Tabla para mostrar datos
tabla = ttk.Treeview(ventana, columns=("Dato"), show="headings")
tabla.heading("Dato", text="Dato Ingresado")
tabla.pack(pady=10, fill=tk.BOTH, expand=True)

# Ejecuta la aplicación
ventana.mainloop()