import random


def generar_contrasena(palabra1, palabra2):
    simbolos = ['!', '@', '#', '$', '%', '&']
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

    return contrasena


# Solicitar las palabras al usuario
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

# Generar la contraseña
contrasena_generada = generar_contrasena(palabra1, palabra2)

# Mostrar la contraseña generada
print("La contraseña generada es:", contrasena_generada)
