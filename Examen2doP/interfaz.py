from tkinter import Tk, messagebox, Label, Entry, BooleanVar, Checkbutton, Button
from matricula import Matricula


def Genera_matricula():
    

    messagebox.showinfo("Matricula", f"")
    
    
#ventana
ventana = Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("600x600")
ventana.configure(bg='#C0D9E8')


nameL=Label(ventana, text="Fecha de nacimiento")
nameL.place(x=30,y=30, width=250, height=30)
nameE=Entry(ventana)
nameE.place(x=120, y=60, width=80, height=40)

ventana.mainloop()