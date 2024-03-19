from tkinter import Tk, ttk, Frame, Button, Label, Entry, messagebox
import sys
from banco import Cta


ventana = Tk()
ventana.title("Manejo de cuentas bancarias")
ventana.geometry("400x300")

# pestañas
panel = ttk.Notebook(ventana)
panel.pack(fill="both", expand="yes")

tab1 = ttk.Frame(panel)
panel.add(tab1, text="Registro de usuarios")

tab2 = ttk.Frame(panel)
panel.add(tab2, text="Consulta de saldo")

tab3 = ttk.Frame(panel)
panel.add(tab3, text="Retiro de efectivo")

tab4 = ttk.Frame(panel)
panel.add(tab4, text="Transferencia de efectivo")

# Funciones para las operaciones
objCta = Cta()

def alta_cuenta():
    print("Ingresa los datos del usuario nuevo\n")
    NoCta = entrada_no_cuenta.get()
    Titular = entrada_titular.get()
    edad = entrada_edad.get()
    saldo = entrada_saldo.get()
    objCta.Alta(NoCta, Titular, edad, saldo)
    messagebox.showinfo("Alta de cuenta", "Titular dado de alta")

def consulta_saldo():
    print("Consulta de saldo")
    NoCta = entrada_no_cuenta_consulta.get()
    Titular = entrada_titular_consulta.get()
    saldo = objCta.ConsultaSaldo(NoCta, Titular)
    if saldo is not None:
        messagebox.showinfo("Consulta de saldo", f"Saldo: {saldo}")
    else:
        messagebox.showwarning("Consulta de saldo", "No se encontró saldo para la cuenta especificada")

def retiro_efectivo():
    print("Retiro de dinero")
    NoCta = entrada_no_cuenta_retiro.get()
    Titular = entrada_titular_retiro.get()
    cantidad = float(entrada_cantidad_retiro.get())
    objCta.retiro(NoCta, Titular, cantidad)
    messagebox.showinfo("Retiro de efectivo", f"Retiro exitoso de: {cantidad} pesos")

# Contenido de la pestaña "Registro de usuarios"
etiqueta_no_cuenta = Label(tab1, text="Numero de cuenta:")
etiqueta_no_cuenta.grid(row=0, column=0)
entrada_no_cuenta = Entry(tab1)
entrada_no_cuenta.grid(row=0, column=1)

etiqueta_titular = Label(tab1, text="Nombre del titular:")
etiqueta_titular.grid(row=1, column=0)
entrada_titular = Entry(tab1)
entrada_titular.grid(row=1, column=1)

etiqueta_edad = Label(tab1, text="Edad del titular:")
etiqueta_edad.grid(row=2, column=0)
entrada_edad = Entry(tab1)
entrada_edad.grid(row=2, column=1)

etiqueta_saldo = Label(tab1, text="Saldo inicial:")
etiqueta_saldo.grid(row=3, column=0)
entrada_saldo = Entry(tab1)
entrada_saldo.grid(row=3, column=1)

boton_alta_cuenta = Button(tab1, text="Alta de cuenta", command=alta_cuenta)
boton_alta_cuenta.grid(row=4, columnspan=2)

# Contenido de la pestaña "Consulta de saldo"
etiqueta_no_cuenta_consulta = Label(tab2, text="Numero de cuenta:")
etiqueta_no_cuenta_consulta.grid(row=0, column=0)
entrada_no_cuenta_consulta = Entry(tab2)
entrada_no_cuenta_consulta.grid(row=0, column=1)

etiqueta_titular_consulta = Label(tab2, text="Titular:")
etiqueta_titular_consulta.grid(row=1, column=0)
entrada_titular_consulta = Entry(tab2)
entrada_titular_consulta.grid(row=1, column=1)

boton_consulta_saldo = Button(tab2, text="Consulta de saldo", command=consulta_saldo)
boton_consulta_saldo.grid(row=2, columnspan=2)

# Contenido de la pestaña "Retiro de efectivo"
etiqueta_no_cuenta_retiro = Label(tab3, text="Numero de cuenta:")
etiqueta_no_cuenta_retiro.grid(row=0, column=0)
entrada_no_cuenta_retiro = Entry(tab3)
entrada_no_cuenta_retiro.grid(row=0, column=1)

etiqueta_titular_retiro = Label(tab3, text="Titular:")
etiqueta_titular_retiro.grid(row=1, column=0)
entrada_titular_retiro = Entry(tab3)
entrada_titular_retiro.grid(row=1, column=1)

etiqueta_cantidad_retiro = Label(tab3, text="Cantidad a retirar:")
etiqueta_cantidad_retiro.grid(row=2, column=0)
entrada_cantidad_retiro = Entry(tab3)
entrada_cantidad_retiro.grid(row=2, column=1)

boton_retiro_efectivo = Button(tab3, text="Retiro de efectivo", command=retiro_efectivo)
boton_retiro_efectivo.grid(row=3, columnspan=2)

# Bucle principal de la interfaz de usuario
ventana.mainloop()
