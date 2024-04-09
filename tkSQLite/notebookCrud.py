from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *
from GeneradorPDF import *
import os
 
objControlador=Controlador()
objPDF = GeneradorPDF()

def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())
    
def busUsuario():
    usuarioBD=objControlador.buscarUsuario(varBus.get())
    if usuarioBD == []:
        messagebox.showwarning("pelaste", "id no existe en BD")
    else:
        consulta.delete(1.0, END)
        consulta.insert(END, usuarioBD)

def busUsuarios():
    usuarios = objControlador.usuariosListaBD()
    user.delete(*user.get_children())
    for usuario in usuarios:
        user.insert("", "end", values=usuario)
    
        
def Change(event):
    tabChange = event.widget.select()
    tabtext = event.widget.tab(tabChange, "text")
    if tabtext == "Consultar usuarios":
        print("Consultar usuarios tab selected!")
        busUsuarios()
        
def ejecutaPDF():
    if varTitulo == []:
        messagebox.showwarning("Importante", "Escribe un nombre al PDF tibio")
    else:
        objPDF.add_page()
        objPDF.chapter_body()
        objPDF.output(varTitulo.get()+".pdf")
        rutaPDF="C:/Users/Lenovo/OneDrive/Documentos/GitHub/FPOO195/"+varTitulo.get()+".pdf"
        messagebox.showinfo("Archivo creado", "PDF disponible en carpeta")
        os.system(f"start {rutaPDF}")


#1.
ventana= Tk()
ventana.title("CRUD de usuarios")
ventana.geometry("600x300")

#2.
panel = ttk.Notebook(ventana)   
panel.pack(fill="both", expand="yes")

#3.
tab1 = ttk.Frame(panel)
tab2 = ttk.Frame(panel)
tab3 = ttk.Frame(panel)
tab4 = ttk.Frame(panel)
tab5 = ttk.Frame(panel)
tab6 = ttk.Frame(panel)

#4. agregar pestanas
panel.add(tab1, text="Agregar usuario")
panel.add(tab2, text="Buscar Usuario")
panel.add(tab3, text="Consultar usuarios")
panel.add(tab4, text="Editar Usuario")
panel.add(tab5, text="Eliminar usuario")
panel.add(tab6, text="Reportes en PDF")

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

#6
Label(tab2, text="Buscar usuarios", fg="red", font=("Mono",18)).pack()

varBus = tk.StringVar()
Label(tab2, text="Id: ").pack()
Entry(tab2, textvariable=varBus).pack()

Button(tab2, text="Buscar usuario", command=busUsuario).pack()

Label(tab2, text="Registrado:", fg="blue", font=("Mono",16)).pack()
consulta = Text(tab2, height=5, width=52)
consulta.pack()

#7 lista de usuarios registrados en BD
Label(tab3, text="Lista de usuarios en BD", fg="black", font=("Mono",18)).pack()
user = ttk.Treeview(tab3, columns=("id", "nombre", "correo"), show="headings")
user.heading("id", text="ID")
user.heading("nombre", text="Nombre")
user.heading("correo", text="Correo")

user.column("id", width=50)
user.column("nombre", width=150)
user.column("correo", width=200)

user.pack()

panel.bind("<<NotebookTabChanged>>", Change)

#8 editar usuario



#9 eliminar usuario



#10generadorPDF
Label(tab6, text="Usuarios en PDF", fg="black", font=("Mono",18)).pack()

varTitulo = tk.StringVar()
Label(tab6, text="Titulo: ").pack()
Entry(tab6, textvariable=varTitulo).pack()

Button(tab6, text="Generar PDF", command=ejecutaPDF).pack()


ventana.mainloop()