from database.connect import connect

def user_exist(chat_id):
    user_id = chat_id
    conn = connect()  # Conectar a la base de datos
    if not conn:
        print("Error de conexión a la base de datos.")
        print("pa")
        return False

    with conn.cursor() as cursor:
        # Consulta para verificar si el usuario existe
        select_query = "SELECT 1 FROM usuarios WHERE ID = %s LIMIT 1;"
        cursor.execute(select_query, (user_id,))
        existe = cursor.fetchone()  # Devuelve None si el usuario no existe

    conn.close()  # Cerrar la conexión
    return bool(existe)  # True si el usuario existe, False si no
