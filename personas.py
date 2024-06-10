from Conexion import *

class Personas:
    def ingresarPersonas(nombre, apellido, sexo):
        try:
            conect = CConexion.ConexionBD()
            cursor = conect.cursor()
            # %s le indica que va a ser un parametro
            sql = "insert into usuarios values (null,%s,%s,%s);" 
            #la variable de valora sera una tupla.
            valores = (nombre, apellido, sexo)
            #cursor agrupa los valores al sql debe ir en el mismo orden
            cursor.execute(sql, valores)
            conect.commit()#manda la informacion a produccion
            print(cursor.rowcount, "registro ingresado")#
            conect.close()#cerramos la conexion


        except mysql.connector.Error as error:
            #informa el error de coneccion a base de dato
            print("Error al conectarce a la base de datos{}".format(error))
            
    