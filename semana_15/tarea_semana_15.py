import tkinter as tk
from tkinter import ttk, messagebox

# Ventana principal
root2 = tk.Tk()
root2.title("Lista de Tareas - Variante 2")
root2.geometry("500x400")

# Lista de tareas
tasks2 = []

# Etiqueta para mostrar el estado de la tarea
status_label = tk.Label(root2, text="", font=("Arial", 10), fg="green")
status_label.pack(pady=5)

# Funciones de eventos
def add_task2(event=None):
    task = entry2.get().strip()
    if task:
        tasks2.append({"text": task, "completed": False})
        update_treeview()
        entry2.delete(0, tk.END)
        status_label.config(text="")
    else:
        messagebox.showwarning("Campo Vacío", "Por favor escribe una tarea.")

def update_treeview():
    for item in tree.get_children():
        tree.delete(item)
    for idx, task in enumerate(tasks2):
        tags = ("completed",) if task["completed"] else ("pending",)
        display_text = task["text"] + (" [Tarea completada]" if task["completed"] else "")
        tree.insert("", "end", iid=idx, text=display_text, tags=tags)

def mark_completed2():
    selected = tree.focus()
    if selected:
        index = int(selected)
        tasks2[index]["completed"] = not tasks2[index]["completed"]
        update_treeview()
        if tasks2[index]["completed"]:
            status_label.config(text="Tarea completada")
        else:
            status_label.config(text="Tarea marcada como pendiente")
    else:
        messagebox.showinfo("Selecciona una tarea", "Debes seleccionar una tarea para marcarla.")

def delete_task2():
    selected = tree.focus()
    if selected:
        index = int(selected)
        del tasks2[index]
        update_treeview()
        status_label.config(text="")
    else:
        messagebox.showinfo("Selecciona una tarea", "Debes seleccionar una tarea para eliminarla.")

# Componentes
title2 = tk.Label(root2, text="Lista de Tareas Moderna", font=("Helvetica", 16))
title2.pack(pady=10)

entry2 = tk.Entry(root2, width=40)
entry2.pack(pady=5)
entry2.bind("<Return>", add_task2)

btn_frame2 = tk.Frame(root2)
btn_frame2.pack(pady=5)

add_btn2 = tk.Button(btn_frame2, text="Añadir", command=add_task2)
add_btn2.grid(row=0, column=0, padx=5)

complete_btn2 = tk.Button(btn_frame2, text="Marcar Completada", command=mark_completed2)
complete_btn2.grid(row=0, column=1, padx=5)

delete_btn2 = tk.Button(btn_frame2, text="Eliminar", command=delete_task2)
delete_btn2.grid(row=0, column=2, padx=5)

# Treeview con colores
style = ttk.Style()
style.configure("Treeview", rowheight=25)
style.map("Treeview")

style.configure("Treeview", font=("Arial", 12))
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

style.configure("Treeview", background="#f0f0f0", fieldbackground="#f0f0f0")

style.map("Treeview", background=[("selected", "#cccccc")])

style.configure("Treeview", foreground="black")

style.map("Treeview", foreground=[
    ("!disabled", "black"),
    ("selected", "blue")
])

# Asociamos colores a tareas completadas
style.configure("completed.Treeview", foreground="green")
style.configure("pending.Treeview", foreground="black")

tree = ttk.Treeview(root2, columns=("Estado",), show="tree")
tree.pack(pady=10, fill="both", expand=True)

tree.tag_configure("completed", foreground="green")
tree.tag_configure("pending", foreground="black")

# Iniciamos la segunda app
root2.mainloop()