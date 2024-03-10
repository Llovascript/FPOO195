from tkinter import Tk, messagebox, Label, Entry, BooleanVar, Checkbutton, Button, Frame
from contraRand import Contraseña

def genera_password():
    length_input = length_entry.get()
    if length_input.strip() == "":
        length = 8
    else:
        length = int(length_input)

    include_uppercase = uppercase_var.get()
    include_special_chars = special_chars_var.get()

    contraseña = Contraseña(length, include_uppercase, include_special_chars)
    password = contraseña.generate_password()
    strength = contraseña.check_password_strength(password) 
    Passw.delete(0, 'end')  
    Passw.insert(0, password)   
    messagebox.showinfo("Contraseña generada", f"La contraseña generada es: {password}\n\nFuerza de la contraseña: {strength}")
    

#ventana
ventana = Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("350x400")
ventana.configure(bg='#C0D9E8')

# Widget
length_label = Label(ventana, text="Longitud del password (8 por defecto)")
length_label.place(x=30, y=30, width=250, height=30)

length_entry = Entry(ventana)
length_entry.place(x=120, y=60, width=50, height=30)

uppercase_var = BooleanVar()
uppercase_checkbox = Checkbutton(ventana, text="¿Incluir mayúsculas?", variable=uppercase_var)
uppercase_checkbox.place(x=50, y=100)

special_chars_var = BooleanVar()
special_chars_checkbox = Checkbutton(ventana, text="¿Incluir caracteres especiales?", variable=special_chars_var)
special_chars_checkbox.place(x=50, y=130)

PasswL= Label(ventana, text="Contraseña generada:")
PasswL.place(x=50, y=160, width=200, height=30)

Passw = Entry(ventana)
Passw.place(x=50, y=200, width=200, height=30)

# Boton
Gbutton = Button(ventana, text="Generar Contraseña", command=genera_password, bg='#0D5CCE', fg='#FFFFFF')
Gbutton.place(x=50, y=250, width=200, height=30)

ventana.mainloop()
