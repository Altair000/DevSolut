from connect import connect

def obtener_datos_usuario(conn, user_id):
    with conn.cursor() as cursor:
        # Consulta SQL para obtener todos los datos del usuario
        select_query = """
            SELECT "User", ID, Registro, Saldo, Rango, exp_rango, Ban
            FROM usuarios
            WHERE ID = %s;
        """
        try:
            cursor.execute(select_query, (user_id,))
            resultado = cursor.fetchone()  # Obtener el primer resultado

            if resultado:
                # Desempaquetar los resultados
                username, user_id, fecha_registro, creditos, rango, exp_rango, estado_ban = resultado
                datos_usuario = {
                    "username": username,
                    "user_id": user_id,
                    "fecha_registro": fecha_registro,
                    "creditos": creditos,
                    "rango": rango,
                    "exp_rango": exp_rango,
                    "estado_ban": estado_ban
                }
                print(f"Datos del usuario con ID {user_id}: {datos_usuario}.")
                return datos_usuario
            else:
                print(f"No se encontró ningún usuario con ID {user_id}.")
                return None

        except Exception as e:
            print(f"Error al obtener los datos del usuario: {e}")
            return None

# Ejemplo de cómo llamar a esta función
def main():
    conn = connect()
    if conn:
        user_id = 123456789  # Este valor vendría del bot
        datos_usuario = obtener_datos_usuario(conn, user_id)
        if datos_usuario:
            print(f"Datos obtenidos: {datos_usuario}")
        conn.close()
