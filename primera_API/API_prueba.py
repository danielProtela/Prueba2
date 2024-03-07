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
    m=[]
    for i in usuario:
        m.append({"Nombre": i[1], "id": i[0]})
    
    return m

@app.route('/API/leert', methods=['GET'])
def leert():
    conexion = mysql.connector.connect(**mysql_prueba)
    # Crear un objeto Cursor para interactuar con la base de datos
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuario = cursor.fetchall()
    cursor.close()
    conexion.close()
    m=[]
    for i in usuario:
        m.append({"Nombre": i[1], "id": i[0], "Contraseña": i[2]})
    
    return m

#Crear entradas en la tabla de usuarios------------------------------------------------
@app.route('/API/crear', methods=['POST'])
def crear():
        try: 
            conexion = mysql.connector.connect(**mysql_prueba)
            # Crear un objeto Cursor para interactuar con la base de datos
            cursor = conexion.cursor()
            datos_recibidos = request.get_json()
            # Ejemplo de datos a insertar
        
            if datos_recibidos and 'nombre' in datos_recibidos and 'contrasena' in datos_recibidos:
                nombre_usuario = datos_recibidos['nombre']
                contrasena_usuario = datos_recibidos['contrasena']

                # Consulta para insertar una entrada en la tabla usuarios
                consulta_insertar = """
                    INSERT INTO usuarios (nombre, contrasena)
                    VALUES (%s, %s)
                """

                # Ejecutar la consulta con los datos
                cursor.execute(consulta_insertar, (nombre_usuario, contrasena_usuario))

                # Confirmar los cambios en la base de datos
                conexion.commit()
            else:
                return jsonify({'error': 'Error creando usuario'})
            return jsonify({'mensaje': 'usuario creado'})
        except mysql.connector.Error as err:
            return jsonify({'error': 'error creando usuario'})
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conexion' in locals():
                conexion.close()
#Modificar datos de la tabla de usuarios-------------------------------------------

@app.route('/API/modificar', methods=['POST'])
def modificar():
    try:
        conexion = mysql.connector.connect(**mysql_prueba)
        # Crear un objeto Cursor para interactuar con la base de datos
        cursor = conexion.cursor()
        # Consulta para eliminar un usuario por ID

        datos_recibidos = request.get_json()
        # Ejemplo de datos a insertar
        
        if datos_recibidos and 'nombre' in datos_recibidos and 'contrasena' in datos_recibidos and 'id' in datos_recibidos:
            nombre_nuevo = datos_recibidos['nombre']
            contrasena_nueva = datos_recibidos['contrasena']
            id_user=datos_recibidos['id']
            consulta_id = "SELECT id FROM usuarios WHERE id = %s"
            cursor.execute(consulta_id, (id_user,))
            if cursor.fetchone():
                consulta_modificar = "UPDATE usuarios SET nombre= %s, contrasena= %s WHERE id = %s"
                # Ejecutar la consulta con el ID proporcionado en la URL
                cursor.execute(consulta_modificar, (nombre_nuevo, contrasena_nueva, id_user))
                # Confirmar los cambios en la base de datos
                conexion.commit()
                return jsonify({'mensaje': f'Usuario con ID {id_user} modificado correctamente'})
            else:
                return jsonify({'error': f'Error, no existe el usuario con ID {id_user}'})
            
        elif datos_recibidos and 'nombre' in datos_recibidos and 'id' in datos_recibidos:
            nombre_nuevo = datos_recibidos['nombre']
            id_user=datos_recibidos['id']
            consulta_id = "SELECT id FROM usuarios WHERE id = %s"
            cursor.execute(consulta_id, (id_user,))
            if cursor.fetchone():
                consulta_modificar = "UPDATE usuarios SET nombre= %s WHERE id = %s"
                # Ejecutar la consulta con el ID proporcionado en la URL
                cursor.execute(consulta_modificar, (nombre_nuevo, id_user))
                # Confirmar los cambios en la base de datos
                conexion.commit()
                return jsonify({'mensaje': f'Usuario con ID {id_user} modificado correctamente'})
            else:
                return jsonify({'error': f'Error, no existe el usuario con ID {id_user}'})
        elif datos_recibidos and 'contrasena' in datos_recibidos and 'id' in datos_recibidos:
            contrasena_nueva = datos_recibidos['contrasena']
            id_user=datos_recibidos['id']
            consulta_id = "SELECT id FROM usuarios WHERE id = %s"
            cursor.execute(consulta_id, (id_user,))
            if cursor.fetchone():
                consulta_modificar = "UPDATE usuarios SET contrasena= %s WHERE id = %s"
                # Ejecutar la consulta con el ID proporcionado en la URL
                cursor.execute(consulta_modificar, (contrasena_nueva, id_user))
                # Confirmar los cambios en la base de datos
                conexion.commit()
                return jsonify({'mensaje': f'Usuario con ID {id_user} modificado correctamente'})
            else:
                return jsonify({'error': f'Error, no existe el usuario con ID {id_user}'})
        else:
            return jsonify({'error': 'Error modificando usuario'})
        

    except mysql.connector.Error as err:
        return jsonify({'error': f'Error en la base de datos: {err}'}), 500  # Código de estado HTTP 500 para "Internal Server Error"

    finally:
        if 'cursor' in locals():
                cursor.close()
        if 'conexion' in locals():
            conexion.close()

#Eliminar datos de la tabla de usuarios
@app.route('/API/eliminar', methods=['POST'])
def eliminar():
    try:
        conexion = mysql.connector.connect(**mysql_prueba)
        # Crear un objeto Cursor para interactuar con la base de datos
        cursor = conexion.cursor()
        # Consulta para eliminar un usuario por ID
        datos_recibidos = request.get_json()
        
        if datos_recibidos and 'id' in datos_recibidos:

            id_user = datos_recibidos['id']
            consulta_id = "SELECT id FROM usuarios WHERE id = %s"
            cursor.execute(consulta_id, (id_user,))
            if cursor.fetchone():

                consulta_eliminar = "DELETE FROM usuarios WHERE id = %s"
                # Ejecutar la consulta con el ID proporcionado en la URL
                cursor.execute(consulta_eliminar, (id_user,))

                # Confirmar los cambios en la base de datos
                conexion.commit()
                return jsonify({'mensaje': f'Usuario con ID {id_user} eliminado correctamente'})
            else:
                return jsonify({"error": f'Error, El usuario con ID {id_user} no existe'})
        else:
            return jsonify({"error": f'Error eliminando usuario, no ID ingresado'})
    except mysql.connector.Error as err:
        return jsonify({'error': f'Error en la base de datos: {err}'}), 500  # Código de estado HTTP 500 para "Internal Server Error"

    finally:
        cursor.close()
        conexion.close()

if __name__ == '__main__':
    app.run(host='192.168.65.18', port=3005, debug=True)


