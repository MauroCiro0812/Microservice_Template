# Importamos para conectar a postgreSQL
import psycopg2

class connection():
    #Creamos la funcion para conectar con la bd
    def connected():
        try:
            #Credenciales de conexion       
            conexion = psycopg2.connect(
                host = 'localhost',
                user = 'postgres',
                password = 'toor',
                database = 'Edemco',
                port = '5432'
            )
            print("successful connection")
        except Exception as ex:
            print(ex)

        #Creamos el cursor para manipular consultas en nuestra bd
        curs = conexion.cursor()
        print('Connection Complete')
        return curs