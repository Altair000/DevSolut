from database.connect import connect

def obtener_rango(conn, user_id):
    with conn.cursor() as cursor:
        # Consulta SQL para obtener el rango del usuario
        select_query = """
            SELECT Rango FROM usuarios WHERE ID = %s;
        """
        try:
            cursor.execute(select_query, (user_id,))
            resultado = cursor.fetchone()  # Obtener el primer resultado

            if resultado:
                rango = resultado[0]  # El rango es el primer elemento del resultado
                print(f"El rango del usuario con ID {user_id} es: {rango}.")
                return rango
            else:
                print(f"No se encontró ningún usuario con ID {user_id}.")
                return None

        except Exception as e:
            print(f"Error al obtener el rango del usuario: {e}")
            return None

# Ejemplo de cómo llamar a esta función
def get_rango(chat_id):
    conn = connect()
    user_id = chat_id
    if conn:
        rango = obtener_rango(conn, user_id)
        if rango:
            print(f"Rango obtenido: {rango}")
            return rango
        conn.close()
