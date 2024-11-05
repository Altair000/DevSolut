import telebot
import os

# Obtener el token del bot
bot_token = os.getenv("TOKEN", "7613090119:AAGfZ5GJ6149Kv9OYIAF6Fb8a2n_WU09B14")

if bot_token:
    # Iniciar el bot con el token obtenido
    bot = telebot.TeleBot(bot_token)

# BOT INFO
bot_info = bot.get_me()
BOT_USERNAME = bot_info.username
BOT_NAME = bot_info.first_name
BOT_ID = bot_info.id