from database.connect import connect

def obtener_creditos(conn, user_id):
    with conn.cursor() as cursor:
        # Consulta SQL para obtener los créditos del usuario
        select_query = """
            SELECT Saldo
            FROM usuarios
            WHERE ID = %s;
        """
        try:
            cursor.execute(select_query, (user_id,))
            resultado = cursor.fetchone()  # Obtener un único resultado
            
            if resultado is not None:
                creditos = resultado[0]
                print(f"El usuario con ID {user_id} tiene {creditos} créditos.")
                return creditos
            else:
                print(f"No se encontró ningún usuario con ID {user_id}.")
                return None
        except Exception as e:
            print(f"Error al obtener los créditos del usuario: {e}")
            return None

# Ejemplo de cómo llamar a esta función
def get_credits(chat_id):
    conn = connect()
    user_id = chat_id
    if conn:
        creditos = obtener_creditos(conn, user_id)
        if creditos is not None:
            print(f"Créditos del usuario {user_id}: {creditos}")
        else:
            print(f"No se pudieron obtener los créditos para el usuario {user_id}.")
        conn.close()
