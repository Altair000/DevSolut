from config.bot_config import bot, Chanel_id
from telebot import types

# Comando /add_credits
def add_credits_handler(bot):    
    @bot.message_handler(commands=['add_credits'])
    def add_credits_command(message):
        bot.send_message(message.chat.id, "💳 Por favor, introduce el user_id del usuario al que deseas agregar créditos.")
        
        # Esperar a que el admin introduzca el user_id
        bot.register_next_step_handler(message, request_credits_amount)

    def request_credits_amount(message):
        try:
            user_id = int(message.text)  # Convertir el user_id ingresado a entero
            bot.send_message(message.chat.id, "💰 Introduce la cantidad de créditos que deseas agregar.")

            # Guardar temporalmente el user_id y pedir la cantidad de créditos
            bot.register_next_step_handler(message, lambda msg: add_credits_to_user(msg, user_id))
        except ValueError:
            bot.send_message(message.chat.id, "⚠️ El ID de usuario debe ser un número. Intenta de nuevo con /add_credits.")
            
    def add_credits_to_user(message, user_id):
        # Convertir la cantidad de créditos ingresada a entero
        creditos = int(message.text)
        sender = str(message.from_user.username)
        # Generar botón inline
        key_button = types.InlineKeyboardButton(text="💱Canjear Créditos💱", callback_data=f"credits_{user_id}_{creditos}")
        keyboard = types.InlineKeyboardMarkup().add(key_button)

        # Enviar el botón al chat del usuario
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(user_id, f"🆙Has recibido un beneficio de {creditos} Créditos. Usa el botón para activarlo.🆙", reply_markup=keyboard)
        bot.send_message(message.chat.id, "🔑 Botón de canje enviado correctamente.")
        bot.send_message(Chanel_id, f"{sender} Ha enviado {creditos} créditos a el usuario con ID: {user_id}")
