from config.bot_config import bot
from database.users_list import users_lister

def users_list(bot):    
    @bot.message_handler(commands=['listar_usuarios'])
    def listar_usuarios_cmd(message):
        chat_id = message.chat.id  # ID del chat del administrador

        # Llamar a la función listar_usuarios para mostrar la primera página de usuarios
        bot.send_chat_action(chat_id, 'typing')
        users_lister(bot, chat_id, pagina=0)
