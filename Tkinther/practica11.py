from tkinter import Tk, Frame, Button, messagebox

#metodo para mensaje
def mostrarMensajes():
    print(messagebox.showinfo('showinfo', 'Information'))
    print(messagebox.showerror('showerror', 'Error'))
    print(messagebox.showwarning('showwarning', 'warning'))
    print(messagebox.askokcancel(message="¿Si o No?", title="Soy el licenciado Marco"))


#

def addbtn():
    botonVerde.config(text="+")
    botonRosa= Button(seccion3,text="Nuevo",bg="#FF33CE")
    botonRosa.configure(height=2,width=5)
    botonRosa.pack()
    
#1.Creamos la ventana
Ventana= Tk() # Uso de poo creando un objeto ventana
Ventana.title("Ejemplo con 3 frames")
Ventana.geometry("600x400")

#2. Colocamos frames de la ventana
seccion1= Frame(Ventana,bg="green")
seccion1.pack(expand= True,fill='both')

seccion2= Frame(Ventana,bg="yellow")
seccion2.pack(expand= True,fill='both')

seccion3= Frame(Ventana,bg="grey")
seccion3.pack(expand= True,fill='both')

#3. Agrega botones

#place
botonAzul= Button(seccion1, text="Azul", fg="#0733f7")
botonAzul.place(x=60,y=60, width=100, height=30)

#grid
botonNegro=Button(seccion2,text="Negro", fg="#FFFFFF", bg="#090909")
botonNegro.configure(height=2,width=10)
botonNegro.grid(row=0,column=1)

botonAmarillo= Button(seccion2,text="Amarillo",bg="#FFE933", command=mostrarMensajes)
botonAmarillo.configure(height=2,width=10)
botonAmarillo.grid(row=1,column=2)

#pack
botonVerde= Button(seccion3,text="Verde",bg="#33FF9C", command=addbtn)
botonVerde.configure(height=2,width=10)
botonVerde.pack()

#Ejecuta la ventana
Ventana.mainloop()