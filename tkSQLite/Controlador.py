from tkinter import messagebox
import sqlite3
import bcrypt

class Controlador:
    def conexion(self):
        try:
            conex=sqlite3.connect("C:/Users/Lenovo/OneDrive/Documentos/GitHub/FPOO195/tkSQLite/db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No jala")
            
    def encriptapass(self, cont):
        passPlana=cont
        passPlana=passPlana.encode()
        sal=bcrypt.gensalt()
        passHash=bcrypt.hashpw(passPlana, sal)
        
        return passHash
    
    def insertUsuario(self, nom, corr, cont):
        
        conexion=self.conexion()
        
        if(nom=="" or corr=="" or cont==""):
            messagebox.showwarning("Cuidado", "inputs vacios no sea tibio")
            conexion.close()
        else:
            cursor= conexion.cursor()
            conH=self.encriptapass(cont)
            datos=(nom, corr, conH)
            sqlInsert="insert into tbUsuarios(nombre, correo, password) values(?,?,?)"
            
            cursor.execute(sqlInsert, datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito", "Eso tilin!!! ")
            
    def buscarUsuario(self, id):
        conex=self.conexion()
        if(id == ''):
            messagebox.showwarning("Cuidado", "inputs vacios no sea tibio")
            conex.close()
        else:
            try:
                cursor=conex.cursor()
                sqlSelect="select * from tbUsuarios where id="+id
                cursor.execute(sqlSelect)
                usuario= cursor.fetchall()
                conex.close()
                return usuario
            except sqlite3.OperationalError:
                print("No se pudo ejecutar la busqueda")
                
    def usuariosListaBD(self):
        conex = self.conexion()
        cursor = conex.cursor()
        try:
            cursor.execute("SELECT * FROM tbUsuarios")
            usuarios = cursor.fetchall()
            conex.close()
            return usuarios
        except sqlite3.OperationalError:
            print("No se pudo ejecutar la busqueda")
            
            
    def buscarUsuarioNom(self, nombre):
        conex=self.conexion()
        if(nombre == ''):
            messagebox.showwarning("Cuidado", "inputs vacios no sea tibio")
            conex.close()
        else:
            try:
                cursor=conex.cursor()
                sqlSelect="select * from tbUsuarios where id="+nombre
                cursor.execute(sqlSelect)
                usuario= cursor.fetchall()
                conex.close()
                return usuario
            except sqlite3.OperationalError:
                print("No se pudo ejecutar la busqueda")
            
    def editarUsuario(self, nombreActual, nuevoNombre, nuevoCorreo, nuevaContra):
        conexion = self.conexion()
        cursor = conexion.cursor()
        try:
            conH = self.encriptapass(nuevaContra)
            cursor.execute("UPDATE tbUsuarios SET nombre=?, correo=?, password=? WHERE nombre=?",
                        (nuevoNombre, nuevoCorreo, conH, nombreActual))
            conexion.commit()
            messagebox.showinfo("Exito", "Usuario actualizado correctamente.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", "Error al editar usuario: " + str(e))
            
    def eliminarUsuario(self, nombreEliminar):
        conexion = self.conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM tbUsuarios WHERE nombre=?", (nombreEliminar,))
            if cursor.rowcount > 0:
                messagebox.showinfo("Exito", f"Usuario '{nombreEliminar}' eliminado correctamente.")
            else:
                messagebox.showwarning("Advertencia", f"No se encontró el usuario '{nombreEliminar}'.")
            conexion.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Error", "Error al eliminar usuario: " + str(e))