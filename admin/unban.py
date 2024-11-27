from config.bot_config import bot, Chanel_id
from database.unban import unban
from telebot import types

# Comando /unban
def unban_handler(bot):    
    @bot.message_handler(commands=['unban'])
    def unban_command(message):
        bot.send_message(message.chat.id, "🔓 Por favor, introduce el user_id del usuario que deseas desbanear.")

        # Esperar a que el admin introduzca el user_id
        bot.register_next_step_handler(message, process_unban_user)

    def process_unban_user(message):
        try:
            user_id = int(message.text)  # Convertir el user_id ingresado a entero

            # Preguntar al administrador si confirma el desbaneo
            confirm_button = types.InlineKeyboardButton(text="🟢 Confirmar Desbaneo 🟢", callback_data=f"confirm_unban_{user_id}")
            cancel_button = types.InlineKeyboardButton(text="❌ Cancelar ❌", callback_data="cancel_unban")
            keyboard = types.InlineKeyboardMarkup().add(confirm_button, cancel_button)

            bot.send_message(message.chat.id, f"⚠️ ¿Estás seguro de que deseas desbanear al usuario con ID {user_id}?", reply_markup=keyboard)
        except ValueError:
            bot.send_message(message.chat.id, "⚠️ El ID de usuario debe ser un número. Intenta de nuevo con /unban.")

# Manejador de callback para confirmar o cancelar el desbaneo
def confirm_unban_handler(bot):    
    @bot.callback_query_handler(func=lambda call: call.data.startswith("confirm_unban") or call.data == "cancel_unban")
    def handle_unban_confirmation(call):
        if call.data == "cancel_unban":
            bot.send_message(call.message.chat.id, "❌ Operación de desbaneo cancelada.")
        else:
            user_id = int(call.data.split("_")[2])  # Extraer el user_id del callback_data
            sender = call.from_user.username
            # Llamar a la función de la base de datos para quitar el ban del usuario
            try:
                unban(user_id)  # Asegúrate de implementar esta función en el módulo de base de datos
                bot.send_message(call.message.chat.id, f"✅ El usuario con ID {user_id} ha sido desbaneado exitosamente.")
                bot.send_message(Chanel_id, f"{sender} ha desbaneado al usuario con ID: {user_id}")
                bot.send_message(user_id, f"✔ Has sido desbaneado por la administración ✔")
            except Exception as e:
                bot.send_message(call.message.chat.id, f"⚠️ Ocurrió un error al intentar desbanear al usuario: {str(e)}")
