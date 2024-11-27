from config.bot_config import bot, Chanel_id, Dev
from database.ban import ban
from telebot import types

# Comando /ban
def ban_handler(bot):    
    @bot.message_handler(commands=['ban'])
    def ban_command(message):
        bot.send_message(message.chat.id, "🚫 Por favor, introduce el user_id del usuario que deseas banear.")

        # Esperar a que el admin introduzca el user_id
        bot.register_next_step_handler(message, process_ban_user)

    def process_ban_user(message):
        try:
            user_id = int(message.text)  # Convertir el user_id ingresado a entero
            if user_id == Dev:
                bot.send_message(message.chat.id, f"Que estás haciendo con tu vida hijo??🙂")
                bot.send_message(Chanel_id, f"El admin {message.from_user.username} ha intentado banear al Desarrollador. Que loco🥵")
                return
            # Preguntar al administrador si confirma el baneo
            confirm_button = types.InlineKeyboardButton(text="🔴 Confirmar Baneo 🔴", callback_data=f"confirm_ban_{user_id}")
            cancel_button = types.InlineKeyboardButton(text="❌ Cancelar ❌", callback_data="cancel_ban")
            keyboard = types.InlineKeyboardMarkup().add(confirm_button, cancel_button)
            
            bot.send_message(message.chat.id, f"⚠️ ¿Estás seguro de que deseas banear al usuario con ID {user_id}?", reply_markup=keyboard)
        except ValueError:
            bot.send_message(message.chat.id, "⚠️ El ID de usuario debe ser un número. Intenta de nuevo con /ban.")

# Manejador de callback para confirmar o cancelar el baneo
def confirm_ban_handler(bot):    
    @bot.callback_query_handler(func=lambda call: call.data.startswith("confirm_ban") or call.data == "cancel_ban")
    def handle_ban_confirmation(call):
        if call.data == "cancel_ban":
            bot.send_message(call.message.chat.id, "❌ Operación de baneo cancelada.")
        else:
            user_id = int(call.data.split("_")[2])  # Extraer el user_id del callback_data
            sender = call.from_user.username

            # Llamar a la función de la base de datos para banear al usuario
            try:
                ban(user_id)  # Asegúrate de implementar esta función en el módulo de base de datos
                bot.send_message(call.message.chat.id, f"✅ El usuario con ID {user_id} ha sido baneado exitosamente.")
                bot.send_message(Chanel_id, f"{sender} Ha baneado a el usuario con ID: {user_id}")
                bot.send_message(user_id, f"❌ Has sido baneado por la administración. Si desea reclamar o saber el motivo del baneo contacte con soporte ❌")
            except Exception as e:
                bot.send_message(call.message.chat.id, f"⚠️ Ocurrió un error al intentar banear al usuario: {str(e)}")
