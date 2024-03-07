import tkinter as tk

def obtener_datos():
    # Esta función se llama cuando se presiona el botón "Enviar"
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()

    # Hacer algo con los datos ingresados, como imprimirlos
    print("Nombre:", nombre)
    print("Edad:", edad)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ingreso de datos")

# Crear etiquetas para los campos de entrada
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0)

etiqueta_edad = tk.Label(ventana, text="Edad:")
etiqueta_edad.grid(row=1, column=0)

# Crear campos de entrada
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1)

entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=1, column=1)

# Crear botón para enviar los datos
boton_enviar = tk.Button(ventana, text="Enviar", command=obtener_datos)
boton_enviar.grid(row=2, column=0, columnspan=2)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
