from admin.set_rango import process_benefit
from config.bot_config import bot

def redeem_handler(bot):    
    @bot.callback_query_handler(func=lambda call: call.data.startswith('redeem_'))
    def redeem_benefit(call):
        bot.send_chat_action(call.message.chat.id, 'typing')
        # Desglosar el callback_data para obtener chat_id, beneficio y tiempo
        data = call.data.split('_')
        user_id = int(data[1])
        beneficio = data[2]
        duracion = data[3]

        # Llamar a la función que otorga el beneficio
        process_benefit(user_id, beneficio, duracion)
        # Informar al usuario y desactivar el botón (eliminar el markup)
        bot.edit_message_text("✅ Beneficio activado con éxito. ✅", call.message.chat.id, call.message.message_id)
