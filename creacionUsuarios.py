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

    # Ejemplo de datos a insertar
    nombre_usuario = "EjemploUsuario"
    contrasena_usuario = "ContraseñaSegura"

    # Consulta para insertar una entrada en la tabla usuarios
    consulta_insertar = """
        INSERT INTO usuarios (nombre, contrasena)
        VALUES (%s, %s)
    """

    # Ejecutar la consulta con los datos
    cursor.execute(consulta_insertar, (nombre_usuario, contrasena_usuario))

    # Confirmar los cambios en la base de datos
    conexion.commit()
 
    
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

