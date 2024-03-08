import mysql.connector

# Configuración de la conexión a la base de datos
mysql_prueba = {
    "host": "10.50.1.34",
    "user": "practicantes",
    "password": "pass",
    "database": "protela_data_cuatro_puntos"   
}

# Conectar a la base de datos
conexion = mysql.connector.connect(**mysql_prueba)

try:
    cursor = conexion.cursor()

    # ID y nombre del rol de prueba
    rol_id = 5  # ID específico que deseas asignar
    rol_prueba = "rol_numero_cinco"

    # Consulta para insertar el rol de prueba en la tabla de roles
    consulta_insertar_rol = """
        INSERT INTO roles (id, rol)
        VALUES (%s, %s)
    """

    # Ejecutar la consulta con el ID y nombre del rol de prueba
    cursor.execute(consulta_insertar_rol, (rol_id, rol_prueba))

    # Confirmar los cambios en la base de datos
    conexion.commit()

    print("Se ha asignado el rol de prueba correctamente.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

