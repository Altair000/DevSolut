from database.connect import connect

def agregar_creditos(conn, user_id, creditos):
    with conn.cursor() as cursor:
        # Consulta SQL para actualizar los créditos del usuario
        update_query = """
            UPDATE usuarios
            SET Saldo = Saldo + %s
            WHERE ID = %s;
        """
        try:
            # Ejecutar la actualización
            cursor.execute(update_query, (creditos, user_id))
            conn.commit()  # Confirmar los cambios en la base de datos
            
            if cursor.rowcount > 0:
                print(f"Se han agregado {creditos} créditos al usuario con ID {user_id}.")
            else:
                print(f"No se encontró ningún usuario con ID {user_id}.")
        except Exception as e:
            print(f"Error al agregar créditos: {e}")
            conn.rollback()  # Revertir los cambios en caso de error

# Ejemplo de cómo llamar a esta función
def add_credits(user_id, creditos):
    conn = connect()
    if conn:
        agregar_creditos(conn, user_id, creditos)
        conn.close()
