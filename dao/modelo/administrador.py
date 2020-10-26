from persona import Persona
class Administrador(Persona):
    def __init__(self,cedula,primerNombre, segundoNombre, primerApellido, segundoApellido, email, contraseña,telefono, direccion,permisos):
        Persopa.__init__(self,cedula,primerNombre, segundoNombre, primerApellido, segundoApellido, email, contraseña,telefono, direccion)
        self.permisos=permisos