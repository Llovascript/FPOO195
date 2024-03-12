from tkinter import Tk, messagebox, Label, Entry, Button
from matricula import Matricula


def Genera_matricula():
    
    messagebox.showinfo("Matricula", f"")
    
    
#ventana
ventana = Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("600x600")
ventana.configure(bg='#C0D9E8')

#fecha de nac
nacL=Label(ventana, text="Fecha de nacimiento")
nacL.place(x=30,y=30, width=250, height=30)
nacE=Entry(ventana)
nacE.place(x=120, y=60, width=80, height=40)

#Nombre
nameL=Label(ventana, text="Nombre")
nameL.place(x=30,y=90, width=250, height=30)
nameE=Entry(ventana)
nameE.place(x=120, y=110, width=80, height=40)

#apellido paterno
apepatL=Label(ventana, text="Apellido Paterno")
apepatL.place(x=30,y=140, width=250, height=30)
apepatE=Entry(ventana)
apepatE.place(x=120, y=160, width=80, height=40)

#apellido materno
apematL=Label(ventana, text="Apellido Materno")
apematL.place(x=30,y=190, width=250, height=30)
apematL=Entry(ventana)
apematL.place(x=120, y=210, width=80, height=40)

#carrera
Carrera=Label(ventana, text="Carrera")
Carrera.place(x=30,y=240, width=250, height=30)
Carrera=Entry(ventana)
Carrera.place(x=120, y=260, width=80, height=40)

Botton = Button(ventana, text="Matricula", command=Genera_matricula, bg='#0D5CCE', fg='#FFFFFF')

ventana.mainloop()