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

    # Objeto cursor para interactuar con la base de datos
    cursor = conexion.cursor()

    # Consulta para insertar una entrada en la tabla usuarios
    consulta_crear_tabla_rol = """
        CREATE TABLE IF NOT EXISTS roles(
            id PRIMARY KEY,
            rol_usuario VARCHAR(255)
        )
    """

    # Ejecutar la consulta
    cursor.execute(consulta_crear_tabla_rol)

    # Confirmar los cambios en la base de datos
    conexion.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar cursor y conexion 
    cursor.close()
    conexion.close()