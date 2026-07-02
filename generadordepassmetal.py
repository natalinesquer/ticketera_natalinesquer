import tkinter as tk
from tkinter import messagebox
import random
import string

def generar_contrasena():
    try:
        longitud = int(entry_longitud.get())

        if longitud < 4 or longitud > 50:
            messagebox.showerror("Error", "La longitud debe ser mayor a 3 y menor o igual a 50.")
            return

        caracteres = string.ascii_letters + string.digits + string.punctuation

        contrasena = ""

        for i in range(longitud):
            contrasena += random.choice(caracteres)

        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, contrasena)

    except:
        messagebox.showerror("Error", "Ingrese un número válido.")


def copiar():
    ventana.clipboard_clear()
    ventana.clipboard_append(entry_resultado.get())
    messagebox.showinfo("Metal", "¡Contraseña copiada!")

ventana = tk.Tk()
ventana.title("🤘 Metal Password Generator 🤘")
ventana.geometry("430x260")
ventana.configure(bg="black")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="🤘 GENERADOR DE CONTRASEÑAS 🤘",
    bg="black",
    fg="red",
    font=("Impact", 16)
)
titulo.pack(pady=10)

tk.Label(
    ventana,
    text="Longitud de la contraseña",
    bg="black",
    fg="white",
    font=("Arial", 11, "bold")
).pack()

entry_longitud = tk.Entry(
    ventana,
    width=10,
    bg="#303030",
    fg="white",
    insertbackground="white",
    justify="center"
)
entry_longitud.pack(pady=5)

boton_generar = tk.Button(
    ventana,
    text="⚡ GENERAR ⚡",
    bg="#8B0000",
    fg="white",
    font=("Arial", 10, "bold"),
    command=generar_contrasena
)
boton_generar.pack(pady=10)


entry_resultado = tk.Entry(
    ventana,
    width=38,
    bg="#202020",
    fg="lime",
    font=("Consolas", 12),
    justify="center",
    insertbackground="white"
)
entry_resultado.pack()


boton_copiar = tk.Button(
    ventana,
    text="💀 COPIAR 💀",
    bg="#505050",
    fg="white",
    font=("Arial", 10, "bold"),
    command=copiar
)
boton_copiar.pack(pady=15)


tk.Label(
    ventana,
    text="Forjado en metal por Natalin Esquer🤘",
    bg="black",
    fg="gray"
).pack()

ventana.mainloop()