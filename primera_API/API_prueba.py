from flask import Flask, jsonify, request
import mysql.connector
import os
# encoding: utf-8
mysql_prueba = {
    "host": "10.50.1.34",
    "user": "practicantes",
    "password": "pass",
    "database": "protela_data_cuatro_puntos"   
}



app = Flask(__name__)

#Ver tablas contenidas en la base de datos-----------------------------------------
@app.route('/API/leerTablasDB', methods=['GET'])
def leerTablasDB():
    conexion = mysql.connector.connect(**mysql_prueba)
    #try:
    
    # Crear un objeto Cursor para interactuar con la base de datos
    cursor = conexion.cursor()

    # Consulta para obtener las tablas en la base de datos
    consulta_tablas = "SHOW TABLES"

    # Ejecutar la consulta
    cursor.execute(consulta_tablas)

    # Obtener los resultados
    tablas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return tablas

#Función para leer tabla de usuarios--------------------------------------------------
@app.route('/API/leer', methods=['GET'])
def leer():
    conexion = mysql.connector.connect(**mysql_prueba)
    # Crear un objeto Cursor para interactuar con la base de datos
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuario = cursor.fetchall()
    cursor.close()
    conexion.close()

    return usuario

#Crear entradas en la tabla de usuarios------------------------------------------------
@app.route('/API/crear', methods=['POST'])
def crear():
        conexion = mysql.connector.connect(**mysql_prueba)
        # Crear un objeto Cursor para interactuar con la base de datos
        cursor = conexion.cursor()
        datos_recibidos = request.get_json()
        # Ejemplo de datos a insertar
        
        if datos_recibidos and 'nombre' in datos_recibidos and 'password' in datos_recibidos:
            nombre_usuario = datos_recibidos['nombre']
            contrasena_usuario = datos_recibidos['password']

        # Consulta para insertar una entrada en la tabla usuarios
        consulta_insertar = """
            INSERT INTO usuarios (nombre, contrasena)
            VALUES (%s, %s)
        """

        # Ejecutar la consulta con los datos
        cursor.execute(consulta_insertar, (nombre_usuario, contrasena_usuario))

        # Confirmar los cambios en la base de datos
        conexion.commit()
        cursor.close()
        conexion.close()

        return jsonify({'mensaje': 'usuario creado'})

#Modificar datos de la tabla de usuarios-------------------------------------------

@app.route('/API/modificar', methods=['PUT'])
def modificar():
    try:
        conexion = mysql.connector.connect(**mysql_prueba)
        # Crear un objeto Cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Consulta para eliminar un usuario por ID
        consulta_modificar = "UPDATE usuarios SET nombre= %s, contrasena= %s WHERE id = %s"
        datos_recibidos = request.get_json()
        # Ejemplo de datos a insertar
        
        if datos_recibidos and 'nombre' in datos_recibidos and 'contrasena' in datos_recibidos and 'id' in datos_recibidos:
            nombre_nuevo = datos_recibidos['nombre']
            contrasena_nueva = datos_recibidos['contrasena']
            id_user=datos_recibidos['id']

        # Ejecutar la consulta con el ID proporcionado en la URL
        cursor.execute(consulta_modificar, (nombre_nuevo, contrasena_nueva, id_user))
        # Confirmar los cambios en la base de datos
        conexion.commit()

        return jsonify({'mensaje': f'Usuario con ID {id_user} modificado correctamente'})

    except mysql.connector.Error as err:
        return jsonify({'error': f'Error en la base de datos: {err}'}), 500  # Código de estado HTTP 500 para "Internal Server Error"

    finally:
        cursor.close()
        conexion.close()

#Eliminar datos de la tabla de usuarios
@app.route('/API/eliminar', methods=['DELETE'])
def eliminar():
    try:
        conexion = mysql.connector.connect(**mysql_prueba)
        # Crear un objeto Cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Consulta para eliminar un usuario por ID
        consulta_eliminar = "DELETE FROM usuarios WHERE id = %s"
        datos_recibidos = request.get_json()
        # Ejemplo de datos a insertar
        
        if datos_recibidos and 'id' in datos_recibidos:
            id_user = datos_recibidos['id']

        # Consulta para insertar una entrada en la tabla usuarios
        consulta_eliminar = """
            INSERT INTO usuarios (id)
            VALUES (%s)
        """
        # Ejecutar la consulta con el ID proporcionado en la URL
        cursor.execute(consulta_eliminar, (id_user,))

        # Confirmar los cambios en la base de datos
        conexion.commit()

        return jsonify({'mensaje': f'Usuario con ID {id_user} eliminado correctamente'})

    except mysql.connector.Error as err:
        return jsonify({'error': f'Error en la base de datos: {err}'}), 500  # Código de estado HTTP 500 para "Internal Server Error"

    finally:
        cursor.close()
        conexion.close()

if __name__ == '__main__':
    app.run(host='192.168.65.15', port=3005, debug=True)


