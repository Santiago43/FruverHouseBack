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
    """
    Clase usuario.
    """
    def __init__(self,cedula,primerNombre, segundoNombre, primerApellido, segundoApellido, email, contraseña,telefono, direccion):
        """
        Constructor de Usuario

        Parámetros:

        cedula -- que es la cédula del usuario.

        primerNombre -- que es el primer nombre del usuario

        segundoNombre -- que es el segundo nombre del usuario

        primerApellido -- que es el primer apellido del usuario

        segundoApellido -- que es el segundo apellido del usuario

        email -- que es el correo electrónico del usuario

        contraseña -- que es la contraseña de acceso del usuario

        teléfono -- que es el teléfono del usuario

        direccion -- que es la direccion del usuario
        """
        Persona.__init__(self,cedula,primerNombre, segundoNombre, primerApellido, segundoApellido, email, contraseña,telefono, direccion)
class Tienda:
    def __init__(self,nombre, direccion):
        self.idTienda=0
        self.nombre=nombre
        self.direccion=direccion

class Categoria:
    def __init__(self,nombre,imagen):
        self.idCategoria=0
        self.nombre=nombre
        self.imagen=imagen

class Producto:
    def __init__(self,idCategoria,nombre,unidad,precio,imagen):
        self.nombre=nombre
        self.unidad=unidad
        self.precio=precio
        self.imagen=imagen
        self.idCategoria=idCategoria
        self.idProducto=0

class Permiso:
    def __init__(self,nombrePermiso):
        self.idPermiso=0
        self.nombrePermiso=nombrePermiso

class Pedido:
    def __init__(self,codigoPedido,idDomiciliario,idUsuario,direccionDestino,listaProductosACompra):
        self.codigoPedido = 0
        self.idDomiciliario=idDomiciliario
        self.idUsuario=idUsuario
        self.direccionDestino=direccionDestino
        self.listaProductosACompra=listaProductosACompra

class ProductoACompra:
    def __init__(self,producto,cantidad):
        self.producto=producto
        self.cantidad=cantidad