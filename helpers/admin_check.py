from database.connect import connect  # Asumimos que ya tienes un módulo connect para gestionar la conexión

def is_admin(user_id):
    """Verifica si el usuario tiene un rango de 'admin' o 'dev' en la base de datos."""
    conn = connect()
    
    if not conn:
        print("Error: No se pudo conectar a la base de datos.")
        return False

    try:
        with conn.cursor() as cursor:
            # Consulta SQL para verificar el rango del usuario
            query = "SELECT Rango FROM usuarios WHERE ID = %s;"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            
            if result:
                rango = result[0]
                # Verifica si el rango es 'admin' o 'dev'
                return rango in ["Admin", "admin", "dev", "Dev"]
            else:
                # Usuario no encontrado en la base de datos
                return False

    except Exception as e:
        print(f"Error al verificar el rango del usuario: {e}")
        return False
    finally:
        conn.close()
