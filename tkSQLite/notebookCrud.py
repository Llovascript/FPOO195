from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

objControlador=Controlador()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())

#1.
ventana= Tk()
ventana.title("CRUD de usuarios")
ventana.geometry("500x300")

#2.
panel = ttk.Notebook(ventana)
panel.pack(fill="both", expand="yes")

#3.
tab1 = ttk.Frame(panel)
tab2 = ttk.Frame(panel)
tab3 = ttk.Frame(panel)
tab4 = ttk.Frame(panel)
tab5 = ttk.Frame(panel)

#4. agregar pestanas
panel.add(tab1, text="Agregar usuario")
panel.add(tab2, text="Buscar Usuario")
panel.add(tab3, text="Consultar usuarios")
panel.add(tab4, text="Editar Usuario")
panel.add(tab5, text="Eliminar usuario")

#5. pestana 1: Formulario insert
Label(tab1, text="Regristo de usuarios", fg="black", font=("Modern",18)).pack()

var1 = tk.StringVar()
Label(tab1, text="Nombre: ").pack()
Entry(tab1, textvariable=var1).pack()

var2 = tk.StringVar()
Label(tab1, text="Correo: ").pack()
Entry(tab1, textvariable=var2).pack()

var3 = tk.StringVar()
Label(tab1, text="Password: ").pack()
Entry(tab1, textvariable=var3).pack()

Button(tab1, text="Guardar usuario", command=ejecutaInsert).pack()

ventana.mainloop()