import mysql.connector
import os


mysql_prueba = {
    "host": "10.50.1.34",
    "user": "practicantes",
    "password": "pass",
    "database": "protela_data_cuatro_puntos"   
}
conexion = mysql.connector.connect(**mysql_prueba)

try:
    
    # Crear un objeto Cursor para interactuar con la base de datos
    cursor = conexion.cursor()

     # Consulta para crear una tabla (ajusta los nombres y tipos de datos según tus necesidades)
    consulta_creacion_tabla = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255),
            contrasena VARCHAR(255)
        )
    """

    # Ejecutar la consulta
    cursor.execute(consulta_creacion_tabla)

    # Confirmar los cambios en la base de datos
    conexion.commit()
 
    
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

