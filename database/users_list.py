from database.connect import connect
from config.bot_config import bot
from telebot import types

# Función para formatear y obtener una página de la lista de usuarios
def obtener_pagina_usuarios(usuarios, pagina, elementos_por_pagina=5):
    inicio = pagina * elementos_por_pagina
    fin = inicio + elementos_por_pagina
    usuarios_pagina = usuarios[inicio:fin]

    lista_usuarios = []
    for usuario in usuarios_pagina:
        username, user_id, rango, exp_rango, fecha_registro, ban_status = usuario
        if ban_status:  # Si el usuario está baneado
            lista_usuarios.append(f"{username}[{user_id}] -> BAN")
        else:
            lista_usuarios.append(
                f"{username}[{user_id}] -> {rango}[{exp_rango.strftime('%d/%m/%Y') if exp_rango else "Hasta que Cristo baje"}] - {fecha_registro.strftime('%d/%m/%Y')}"
            )
    return "\n".join(lista_usuarios)

# Función principal para listar usuarios con botones de paginación
def users_lister(bot, chat_id, pagina):
    conn = connect()
    if conn:
        with conn.cursor() as cursor:
            # Consulta SQL para obtener todos los usuarios junto con su estado de baneo
            select_query = """
                SELECT "User", ID, Rango, exp_rango, Registro, Ban
                FROM usuarios;
            """
            try:
                cursor.execute(select_query)
                usuarios = cursor.fetchall()  # Obtener todos los registros

                if not usuarios:
                    bot.send_message(chat_id, "No hay usuarios registrados.")
                    return

                # Total de páginas
                total_paginas = (len(usuarios) - 1) // 5 + 1

                # Formatear la página actual de usuarios
                mensaje = obtener_pagina_usuarios(usuarios, pagina)

                # Crear botones de paginación y eliminar
                botones = types.InlineKeyboardMarkup()
                if pagina > 0:
                    botones.add(types.InlineKeyboardButton("⬅️ Anterior", callback_data=f"pagina_{pagina - 1}"))
                if pagina < total_paginas - 1:
                    botones.add(types.InlineKeyboardButton("➡️ Siguiente", callback_data=f"pagina_{pagina + 1}"))
                botones.add(types.InlineKeyboardButton("❌ Eliminar", callback_data="eliminar_mensaje"))

                # Enviar el mensaje con los usuarios y los botones
                bot.send_message(chat_id, mensaje, reply_markup=botones)

            except Exception as e:
                print(f"Error al listar usuarios: {e}")
                bot.send_message(chat_id, "Error al obtener la lista de usuarios.")
            finally:
                conn.close()

# Handler para los callbacks de paginación y eliminar mensaje
@bot.callback_query_handler(func=lambda call: call.data.startswith("pagina_") or call.data == "eliminar_mensaje")
def manejar_paginacion(call):
    if call.data == "eliminar_mensaje":
        bot.delete_message(call.message.chat.id, call.message.message_id)
    else:
        pagina = int(call.data.split("_")[1])
        users_lister(bot, call.message.chat.id, pagina)
