from database.connect import connect
from datetime import datetime, timedelta

def otorgar_rango_premium(conn, user_id, duracion):
    with conn.cursor() as cursor:
        # Calcular la fecha de expiración
        fecha_expiracion = datetime.now() + timedelta(days=duracion)

        # Consulta SQL para actualizar el rango y la fecha de expiración del usuario
        update_query = """
            UPDATE usuarios
            SET Rango = 'Premium', exp_rango = %s
            WHERE ID = %s;
        """
        try:
            cursor.execute(update_query, (fecha_expiracion.strftime('%Y-%m-%d'), user_id))
            conn.commit()  # Confirmar los cambios en la base de datos
            print(f"El rango del usuario con ID {user_id} ha sido actualizado a 'Premium' hasta {fecha_expiracion.strftime('%d/%m/%Y')}.")
        except Exception as e:
            print(f"Error al otorgar rango premium: {e}")
            conn.rollback()  # Revertir los cambios en caso de error

# Ejemplo de cómo llamar a esta función
def set_premium(user_id, duracion):
    conn = connect()
    if conn:
        otorgar_rango_premium(conn, user_id, duracion)
        conn.close()
