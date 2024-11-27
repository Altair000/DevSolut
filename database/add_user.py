from datetime import datetime
from database.connect import connect
from config.bot_config import bot, Chanel_id

def agregar_usuario(conn, username, user_id):
    with conn.cursor() as cursor:
        # Datos del usuario
        fecha_registro = datetime.now().date()  # Fecha de registro actual
        saldo_inicial = 0  # Saldo inicial
        rango_inicial = 'Free'  # Rango inicial
        exp_rango = None  # Sin fecha de expiración inicial
        ban_estado = False  # Estado de ban inicial

        # Consulta SQL para insertar el nuevo usuario
        insert_query = """
            INSERT INTO usuarios ("User", ID, Registro, Saldo, Rango, exp_rango, Ban)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (ID) DO NOTHING;  -- No hacer nada si el usuario ya existe
        """

        try:
            cursor.execute(insert_query, (username, user_id, fecha_registro, saldo_inicial, rango_inicial, exp_rango, ban_estado))
            conn.commit()
            bot.send_message(Chanel_id, f"Usuario {username} registrado correctamente.")
        except Exception as e:
            print(f"Error al agregar el usuario: {e}")
            conn.rollback()  # Revierte cambios en caso de error

# Ejemplo de cómo llamar a esta función
def add_user(chat_id, username):
    user_id = chat_id
    conn = connect()
    if conn:
        print("pp")
        agregar_usuario(conn, username, user_id)
        conn.close()
