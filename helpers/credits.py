from config.bot_config import bot
from database.add_credits import add_credits

def credits_handler(bot):    
    @bot.callback_query_handler(func=lambda call: call.data.startswith('credits_'))
    def redeem_benefit(call):
        bot.send_chat_action(call.message.chat.id, 'typing')
        # Desglosar el callback_data para obtener chat_id, beneficio y tiempo
        data = call.data.split('_')
        user_id = int(data[1])
        creditos = data[2]

        # Llamar a la función que otorga el beneficio
        add_credits(user_id, creditos)
        # Informar al usuario y desactivar el botón (eliminar el markup)
        bot.edit_message_text("✅ Créditos adquiridos con éxito. ✅", call.message.chat.id, call.message.message_id)
