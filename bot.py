from helpers.register_handlers import register_handlers
from config.bot_config import bot
from users.callback_handlers import register_callback_handlers
from users.command_handlers import register_command_handlers

# Main
if __name__ == "__main__":
    register_handlers(bot)  # This will include all command handlers
    register_command_handlers(bot)
    register_callback_handlers(bot)
    bot.infinity_polling()
