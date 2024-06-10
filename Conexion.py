#descargamos el conector pip mysql-conector-python
import mysql.connector

class CConexion:
    def ConexionBD():
        try:
            conexion = mysql.connector.connect(user = '',
                                               password ='',
                                               host='',
                                               database ='',
                                               port='')
            print("Conectado a la base de datos")
            #
            return conexion
        except mysql.connector.Error as error:
            #informa el error de coneccion a base de dato
            print("Error al conectarce a la base de datos{}".format(error))
            return conexion
        
    ConexionBD()