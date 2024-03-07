from tkinter import Tk, Frame, Button, messagebox
from main import *

class ventana:
    
    ventana=Tk()
    ventana.title("login")
    ventana.geometry("400x600")
    
    btn1=Button(ventana, text='Registro', bg='#000000', fg='white', command= agregar_usuario)
    btn1.pack()

    ventana.mainloop()