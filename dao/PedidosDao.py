import mysql.connector
from mysql.connector import errorcode
from dao.dao import dao
from dao.models import Pedido
class PedidosDao(dao):
    def registrar(self,pedido):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "insert into PEDIDO (USUARIO_PERSONA_idPERSONA,direccionDestino) values (%s,%s);"
            cursor.execute(sql,(pedido.idUsuario,pedido.direccionDestino))
            cnx.commit()
            sql2="select codigoPedido from PEDIDO order by codigoPedido desc limit 1;"
            cursor.execute(sql2)
            codigoPedido = cursor.fetchone()
            for producto in pedido.listaProductosACompra:
                sql = "insert into PEDIDO_has_PRODUCTO (PEDIDO_codigoPedido,PRODUCTO_idPRODUCTO,cantidad)values (%s,%s,%s);"
                cursor.execute(sql,(codigoPedido,producto.producto,producto.cantidad))
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return False