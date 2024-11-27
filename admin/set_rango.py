from database import set_admin, set_premium
from config.bot_config import bot, Chanel_id
from telebot import types

# Comando /set_rango
def set_rango_handler(bot):    
    @bot.message_handler(commands=['set_rango'])
    def set_rango(message):
        # Crear botones inline para los rangos
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Premium", callback_data="rango_premium"))
        keyboard.add(types.InlineKeyboardButton(text="Admin", callback_data="rango_admin"))
        
        bot.send_message(message.chat.id, "🔄 Selecciona el rango que deseas establecer:", reply_markup=keyboard)

# Manejar la selección del rango
def rango_handler(bot):    
    @bot.callback_query_handler(func=lambda call: call.data.startswith("rango_"))
    def handle_rango_selection(call):
        rango = call.data.split("_")[1]  # Extraer el rango seleccionado
        bot.send_message(call.message.chat.id, "🔄 Por favor, introduce la duración del rango (ej. '10 días', '30 días').")
        
        # Guardar temporalmente el rango seleccionado para usarlo después
        bot.register_next_step_handler(call.message, lambda msg: set_user_rango(msg, rango))

    def request_user_id(message, rango):
        duracion = message.text  # Obtener la duración introducida por el administrador
        bot.send_message(message.chat.id, "🔄 Ahora, por favor introduce el user_id del usuario al que se le otorgará el beneficio.")
        
        # Guardar temporalmente la duración del rango
        bot.register_next_step_handler(message, lambda msg: set_user_rango(msg, rango, duracion))

    def set_user_rango(message, rango, duracion):
        user_id = int(message.text)  # Obtener el user_id introducido por el administrador
        sender = message.chat.id
        # Generar botón inline
        key_button = types.InlineKeyboardButton(text="💱Canjear beneficio💱", callback_data=f"redeem_{user_id}_{rango}_{duracion}")
        keyboard = types.InlineKeyboardMarkup().add(key_button)

        # Enviar el botón al chat del usuario
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(user_id, f"🆙Has recibido un beneficio de {rango} por {duracion}. Usa el botón para activarlo.🆙", reply_markup=keyboard)
        bot.send_message(Chanel_id, f"{sender} ha otorgado privilegios de {rango} por {duracion} días al usuario con ID: {user_id}")
        bot.send_message(message.chat.id, "🔑 Botón de canje enviado correctamente.")

def process_benefit(user_id, beneficio, duracion):
    if beneficio == 'Premium':
        # Lógica para añadir estado Premium al usuario
        set_premium(user_id, duracion)
    elif beneficio == 'Admin':
        # Lógica para hacer admin al usuario
        set_admin(user_id, duracion)
    else:
        # Otro tipo de beneficio
        pass
