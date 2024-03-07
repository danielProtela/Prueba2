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

    """"
    # Consulta para obtener las tablas en la base de datos
    consulta_tablas = "SHOW TABLES"

    # Ejecutar la consulta
    cursor.execute(consulta_tablas)

    # Obtener los resultados
    tablas = cursor.fetchall()

    # Imprimir el nombre de las tablas
    
    print("Tablas en la base de datos:")
    for tabla in tablas:
        print(tabla[0])
    """
    """"
    cursor.execute("SELECT * FROM incremento")
    columnas = cursor.column_names
    print(columnas)

    usuario = cursor.fetchone()
    print("Tabla de incremento:")
    for user in usuario:
        print(user)

    

    #Consulta de la primera fila de la tabla de incremento
    consulta_update = "UPDATE incremento SET OPERACION = 333 WHERE CENTRO_TRABAJO = '10631034' "


    # Ejecutar la consulta
    cursor.execute(consulta_update)

    # Confirmar los cambios en la base de datos
    conexion.commit()
    
    cursor.execute("SELECT * FROM incremento")
    usuario = cursor.fetchone()
    print("Tabla de incremento:")
    for user in usuario:
        print(user)
    """
     # Consulta para crear una tabla (ajusta los nombres y tipos de datos según tus necesidades)
    consulta_creacion_tabla = """
        CREATE TABLE IF NOT EXISTS ejemplo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        edad INT
    )
    """

    # Ejecutar la consulta
    cursor.execute(consulta_creacion_tabla)

    # Confirmar los cambios en la base de datos
    conexion.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()   
    
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar el cursor y la conexión
    
    conexion.close()

