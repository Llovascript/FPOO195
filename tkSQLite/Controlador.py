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