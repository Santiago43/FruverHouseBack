class Persona:
    def __init__(self,cedula,primerNombre, segundoNombre, primerApellido, segundoApellido, email, contraseña,telefono, direccion):
        self.primerNombre=primerNombre
        self.segundoNombre=segundoNombre
        self.primerApellido=primerApellido
        self.segundoApellido=segundoApellido
        self.email=email
        self.contraseña=contraseña
        self.telefono=telefono
        self.direccion=direccion
        self.cedula=cedula
    

class Administrador(Persona):
    def __init__(self,cedula,primerNombre, segundoNombre, primerApellido, segundoApellido, email, contraseña,telefono, direccion,permisos):
        Persona.__init__(self,cedula,primerNombre, segundoNombre, primerApellido, segundoApellido, email, contraseña,telefono, direccion)
        self.permisos=permisos

class Domiciliario(Persona):
    def __init__(self,cedula,primerNombre, segundoNombre, primerApellido, segundoApellido, email, contraseña,telefono, direccion,idTienda):
        Persona.__init__(self,cedula,primerNombre, segundoNombre, primerApellido, segundoApellido, email, contraseña,telefono, direccion)
        self.idTienda = idTienda

class Usuario(Persona):
    def __init__(self,cedula,primerNombre, segundoNombre, primerApellido, segundoApellido, email, contraseña,telefono, direccion):
        Persona.__init__(self,cedula,primerNombre, segundoNombre, primerApellido, segundoApellido, email, contraseña,telefono, direccion)
