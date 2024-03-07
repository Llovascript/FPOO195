class Usuario:
    usuarios = []

    def __init__(self, nom, corr, pas):
        self.__nombre = nom
        self.__correo = corr
        self.__password = pas
        Usuario.usuarios.append(self)

    def agregar(self):
        print("Usuario agregado:")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")
        print(f"Contraseña: {self.__password}")

    def consultar(self):
        print("Información del usuario:")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")

    def editar(self, nom, corr, pas):
        self.__nombre = nom
        self.__correo = corr
        self.__password = pas
        print("Usuario editado.")
        
    def validar(self, corr, pas):
        if self.__correo == corr and self.__password == pas:
            print(f"Bienvenido {self.__nombre}")
        else:
            print("usuario o contraseña incorrecto")

    def eliminar(self):
        Usuario.usuarios.remove(self)
        print("Usuario eliminado exitosamente.")


