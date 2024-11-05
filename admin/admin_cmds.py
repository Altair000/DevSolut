from config.bot_config import bot
from helpers.admin_check import is_admin
from telebot import types

# Definimos el manejador para el comando /admin_help
def admin_help_handler(bot):    
    @bot.message_handler(commands=['admin_help'])
    def admin_help(message):
        # Solo permite el comando si el usuario es un administrador
        user_id = message.from_user.id
        
        if not is_admin(user_id):
            bot.send_message(message.chat.id, "⛔ No tienes permisos para acceder a los comandos de administrador.")
            return

        # Mensaje con la lista de comandos de administrador
        help_text = (
            "👮‍♂️ Comandos de Administrador:\n\n"
            "/admin_help - Muestra este mensaje de ayuda\n"
            "/set_rango - Establece un rango para un usuario\n"
            "/add_creditos - Agrega créditos a un usuario\n"
            "/ban - Banea a un usuario\n"
            "/unban - Desbanea a un usuario\n"
            "/listar_usuarios - Muestra una lista de todos los usuarios\n"
            "/remove_msg - Elimina un mensaje específico del chat\n"
            "/verificar_usuario - Verifica si un usuario está en la base de datos\n"
        )

        # Crea un botón inline para cerrar el mensaje de ayuda
        markup = types.InlineKeyboardMarkup()
        close_button = types.InlineKeyboardButton(text="❌ Cerrar", callback_data="close_help")
        markup.add(close_button)

        # Enviar el mensaje de ayuda con el botón inline
        bot.send_message(message.chat.id, help_text, reply_markup=markup)

# Manejador para el botón de cierre de ayuda
def close_help_handler(bot):    
    @bot.callback_query_handler(func=lambda call: call.data == "close_help")
    def close_help_message(call):
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            print(f"Error al eliminar el mensaje de ayuda: {e}")
