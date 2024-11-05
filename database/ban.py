from database.connect import connect

def banear_usuario(conn, user_id):
    with conn.cursor() as cursor:
        # Consulta SQL para actualizar el estado de ban
        update_query = """
            UPDATE usuarios
            SET Ban = TRUE
            WHERE ID = %s;
        """
        try:
            cursor.execute(update_query, (user_id,))
            conn.commit()  # Confirmar los cambios en la base de datos
            if cursor.rowcount > 0:
                print(f"Usuario con ID {user_id} ha sido baneado exitosamente.")
                return True
            else:
                print(f"No se encontró ningún usuario con ID {user_id}.")
                return False
        except Exception as e:
            print(f"Error al banear al usuario: {e}")
            conn.rollback()  # Revertir cambios en caso de error
            return False

# Ejemplo de cómo llamar a esta función
def ban(user_id):
    conn = connect()
    if conn:
        if banear_usuario(conn, user_id):
            print(f"El usuario {user_id} ha sido baneado.")
        else:
            print(f"No se pudo banear al usuario {user_id}.")
        conn.close()
