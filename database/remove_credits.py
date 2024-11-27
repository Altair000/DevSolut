from connect import connect

def retirar_creditos(conn, user_id, cantidad):
    with conn.cursor() as cursor:
        # Consulta SQL para obtener el saldo actual del usuario
        select_query = "SELECT Saldo FROM usuarios WHERE ID = %s;"
        cursor.execute(select_query, (user_id,))
        saldo_actual = cursor.fetchone()

        if saldo_actual is not None:
            saldo_actual = saldo_actual[0]
            if saldo_actual >= cantidad:
                # Consulta SQL para actualizar los créditos del usuario
                update_query = """
                    UPDATE usuarios
                    SET Saldo = Saldo - %s
                    WHERE ID = %s;
                """
                try:
                    # Ejecutar la actualización
                    cursor.execute(update_query, (cantidad, user_id))
                    conn.commit()  # Confirmar los cambios en la base de datos
                    print(f"Se han retirado {cantidad} créditos del usuario con ID {user_id}.")
                except Exception as e:
                    print(f"Error al retirar créditos: {e}")
                    conn.rollback()  # Revertir los cambios en caso de error
            else:
                print(f"No se puede retirar {cantidad} créditos. Saldo actual: {saldo_actual}.")
        else:
            print(f"No se encontró ningún usuario con ID {user_id}.")

# Ejemplo de cómo llamar a esta función
def main():
    conn = connect()
    if conn:
        user_id = 123456789  # Este valor vendría del bot
        cantidad = 30  # Créditos a retirar
        retirar_creditos(conn, user_id, cantidad)
        conn.close()
