from tkinter import Tk, messagebox, Label, Entry, BooleanVar, Checkbutton, Button
from contraRand import Contraseña

def generate_and_print_password():
    length_input = length_entry.get()
    if length_input.strip() == "":
        length = 8
    else:
        length = int(length_input)

    include_uppercase = uppercase_var.get()
    include_special_chars = special_chars_var.get()

    contraseña = Contraseña(length, include_uppercase, include_special_chars)
    password = contraseña.generate_password()
    generated_password_label.config(text="Contraseña: " + password)

    strength = contraseña.check_password_strength(password)
    strength_label.config(text="Fuerza: " + strength)

#ventana
ventana = Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x200")

#Widget
length_label = Label(ventana, text="Longitud del password (enter para 8 por default):")
length_label.grid(row=0, column=0, sticky="w")
length_entry = Entry(ventana)
length_entry.grid(row=0, column=1)


def opciones():
    print(messagebox.askokcancel(message="¿Incluir mayúsculas?"), variable=uppercase_var)

uppercase_var = BooleanVar()
uppercase_checkbox = Checkbutton(ventana, text="¿Incluir mayúsculas?", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=0, sticky="w")

special_chars_var = BooleanVar()
special_chars_checkbox = Checkbutton(ventana, text="¿Incluir caracteres especiales?", variable=special_chars_var)
special_chars_checkbox.grid(row=2, column=0, sticky="w")

#boton
opc_button= Button(ventana, text='opciones', bg='#FFE933', command=opciones)
opc_button.configure(height=2, width=10)
opc_button.pack()

generate_button = Button(ventana, text="Generar Contraseña", command=generate_and_print_password, bg='#0D5CCE', fg='#FFFFFF')
generate_button.grid(row=3, column=0, columnspan=2)


#contraseña y fortaleza
generated_password_label = Label(ventana, text="")
generated_password_label.grid(row=4, column=0, columnspan=2)

strength_label = Label(ventana, text="")
strength_label.grid(row=5, column=0, columnspan=2)

ventana.mainloop()
