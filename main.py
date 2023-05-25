import random
import string
import tkinter as tk


def generar_contrasena():
    palabra1 = entry_palabra1.get()
    palabra2 = entry_palabra2.get()

    simbolos = '!@#$%&'

    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    contrasena = ''

    # Agregar caracteres de las palabras
    contrasena += palabra1 + palabra2

    # Agregar símbolos aleatorios
    for _ in range(2):
        contrasena += random.choice(simbolos)

    # Mezclar la contraseña
    contrasena = ''.join(random.sample(contrasena, len(contrasena)))

    label_contrasena.config(text="Contraseña generada: " + contrasena)

    # Guardar la contraseña en un archivo de texto
    nombre_archivo = entry_nombre.get()
    with open(nombre_archivo + ".txt", "w") as file:
        file.write("Contraseña: " + contrasena)


# Crear la ventana principal
window = tk.Tk()
window.title("Generador y Guardador de Contraseñas")

# Etiqueta y campo de entrada para la nombre del archivo
label_nombre = tk.Label(window, text="Nombre del archivo:")
label_nombre.pack()
entry_nombre = tk.Entry(window)
entry_nombre.pack()

# Etiqueta y campo de entrada para la primera palabra
label_palabra1 = tk.Label(window, text="Palabra 1:")
label_palabra1.pack()
entry_palabra1 = tk.Entry(window)
entry_palabra1.pack()

# Etiqueta y campo de entrada para la segunda palabra
label_palabra2 = tk.Label(window, text="Palabra 2:")
label_palabra2.pack()
entry_palabra2 = tk.Entry(window)
entry_palabra2.pack()

# Botón para generar la contraseña y guardarla
button_generar = tk.Button(window, text="Generar y Guardar Contraseña", command=generar_contrasena)
button_generar.pack()

# Etiqueta para mostrar la contraseña generada
label_contrasena = tk.Label(window, text="")
label_contrasena.pack()

# Iniciar el bucle principal de la ventana
window.mainloop()