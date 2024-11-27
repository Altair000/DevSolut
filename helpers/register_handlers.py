from admin.add_credits import add_credits_handler
from admin.admin_cmds import admin_help_handler, close_help_handler
from admin.ban import ban_handler, confirm_ban_handler
from admin.set_rango import rango_handler, set_rango_handler
from admin.unban import confirm_unban_handler, unban_handler
from admin.users_list import users_list
from helpers.credits import credits_handler
from helpers.redeem import redeem_handler

def register_handlers(bot):
    add_credits_handler(bot)
    admin_help_handler(bot)
    close_help_handler(bot)
    ban_handler(bot)
    confirm_ban_handler(bot)
    set_rango_handler(bot)
    rango_handler(bot)
    unban_handler(bot)
    confirm_unban_handler(bot)
    users_list(bot)
    credits_handler(bot)
    redeem_handler(bot)
    