import psycopg2
from config.db_config import dbname, user, password, host

def connect():
    try:
        # Conexión a la base de datos
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port="5432"
        )
        print("Conexión exitosa a la base de datos.")
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
