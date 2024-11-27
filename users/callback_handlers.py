from config.bot_config import bot, BOT_NAME
from database.get_credits import get_credits
from database.get_rango import get_rango
from telebot import types, TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

#Crear menú principal
def create_main_keyboard():
    main_keyboard = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton("• Cuenta •", callback_data="cuenta")
    #b2 = InlineKeyboardButton("• Gateways •", callback_data="gateways")
    b3 = InlineKeyboardButton("• Tools •", callback_data="tools")
    b4 = InlineKeyboardButton("• Planes y Precios •", callback_data="precios")
    b5 = InlineKeyboardButton("• Canal Oficial •", url='https://t.me/+UggxblGvjyY3NDZh')
    main_keyboard.add(b1, b3, b4, b5)
    return main_keyboard

def create_back_keyboard():
    back_keyboard = InlineKeyboardMarkup()
    back_button = InlineKeyboardButton("• Atrás •", callback_data="atras")
    back_keyboard.add(back_button)
    return back_keyboard
  
# Define el manejador de callbacks para la Opción 1
@bot.callback_query_handler(func=lambda call: call.data == "cuenta")
def handle_opción1(call):
    bot.send_chat_action(call.message.chat.id, 'typing')
    user = call.from_user
    chat_id = call.message.chat.id
    user_info = f""" ===============================
          🤖 INFORMACIÓN DE USUARIO 🤖
          🆔 ID: <code>{user.id}</code>
          💵 Créditos: {get_credits(chat_id)}
          👑 Rango: {get_rango(chat_id)}
        ===============================
          """

    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=user_info,
        reply_markup=create_back_keyboard(),  # Agrega el botón "Atrás"
        parse_mode="HTML"
    )

@bot.callback_query_handler(func=lambda call: call.data == "atras")
def handle_back(call):
    bot.send_chat_action(call.message.chat.id, 'typing')
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f'''=========================|
            🤖 {BOT_NAME} 🤖
         
            Si tienes algún problema o
            necesitas ayuda no dudes en
            contactar a mi programador😃
         
            By: <a href="https://t.me/alltallr">@Altaïr</a>
            =========================|
            ''',
        reply_markup=create_main_keyboard(),  # Regresa al teclado principal
        parse_mode="HTML",
        disable_web_page_preview=True
    )

# Define el manejador de callbacks para la opción3
@bot.callback_query_handler(func=lambda call: call.data == 'tools')
def handle_opcion3(call):
    bot.send_chat_action(call.message.chat.id, 'typing')
    tools_text=f'''======================|
                ✥ TOOLS ✥

           ✘ Información del usuario
           ‣ Comando: /info
           ‣ Ejemplo: /info
           ‣ Info: Muestra información sobre el perfil

           ✘ Generar Países aleatorios
           ‣ Comando: /countries
           ‣ Ejemplo: /countries
           ‣ Info: Muestra una lista de paises y su código correspondiente

           ✘ Random Fake Información
           ‣ Comando: /rand
           ‣ Ejemplo: /rand US(código de país proporcionado por el cmd '/countries')
           ‣ Info: Muestra información 
           aleatoria.

           ✘ Extra Gen
           ‣ Comando: /extra
           ‣ Ejemplo: /extra 445100(bin o cc)
           ‣ Info: Crea un extra a partir de un bin o una cc.
           
           ✘ Bin Información
           ‣ Comando: /bin
           ‣ Ejemplo: /bin 445100
           ‣ Info: Muestra información 
           detallada acerca de un Bin.

           ✘ Generar CC'S
           ‣ Comando: /gen
           ‣ Ejemplo: /gen 445100
           ‣ Info: Genera 10 CC'S a partir de un Bin o Extra.
        =======================|
        '''
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=tools_text,
        reply_markup=create_back_keyboard(),
        disable_web_page_preview=True,
        parse_mode="HTML"
    )

# Define el manejador de callbacks para la opción4
def create_prices_main_keyboard():
    prices_main_keyboard = InlineKeyboardMarkup(row_width=0)
    credit_button = InlineKeyboardButton("• Créditos •", callback_data="creditos")
    plus_button = InlineKeyboardButton("• Plus •", callback_data="plus")
    buy_button = InlineKeyboardButton("• Buy •", url='https://t.me/alltallr')
    prices_main_keyboard.add(credit_button, plus_button, buy_button)
    return prices_main_keyboard

combined_keyboard = types.InlineKeyboardMarkup()
combined_keyboard.add(types.InlineKeyboardButton("✥ Buy ✥", url='https://t.me/alltallr'))
    
combined_keyboard.add(types.InlineKeyboardButton("• Atrás •", callback_data='atras'))

@bot.callback_query_handler(func=lambda call: call.data == 'precios')
def handle_opcion4(call):
    bot.send_chat_action(call.message.chat.id, 'typing')
    precios_text=f'''================================|
            ✥ Planes & Precios ✥

        ▹ Para realizar la compra de alguna     
        Subscripción o Paquete de Créditos,
        presione el botón de ✥ Buy ✥ 
        y será dirijido hacia el admin.

        ♖ Métodos de Pago ♖
        ▹ Peso Cubano (transferencia)
        ▹ USD (transferencia)
        ▹ Pago Móvil


        ♛ Subscripción Plus ♛
        ▸ Acceso a gateways MASS.
        ▸ Descuento exclusivos en la compra de Créditos.
		  ▸ Mayor eficiencia en la verificación de tarjetas.
		  ▸ Acceso al Scrapper (3h x día).
		  ▸ Acceso al canal de bins.
		  ▸ Sorteo de créditos (50-100)
		
		  ♛ Subscripción Plus+ ♛
		  ▸ Mismas ventajas de la subscripción Plus.
		  ▸ La eficiencia de verificación mejora. considerablemente al utilizar proxies tipo élite.
		  ▸ Acceso 24h al Scrapper.
		  ▸ Herramientas como "gen" y "bin" son gratis.
		  ▸ Acceso al canal de Bins premium.
		  ▸ Sorteo de créditos (150-250).
		  ▸ 3 días de Prueba gratuita del bot OTP previa a su fecha de lanzamiento.


        ✥ Subscripción Plus ✥

🜲 10/días = $5.00 USD
+25/créditos de Regalo.

🜲 20/días = $8.50 USD
+50/créditos de Regalo.

        ✥ Subscripción Plus+ ✥
🜲  10/días = $10.00 USD
+75/créditos de Regalo.

🜲 20/días = $17.50 USD
+125/créditos de Regalo.

        🜲 Créditos 🜲
        ▸ Acceso a todos los comandos no premium.
        ▸ Acceso al casino.
        ▸ Posibilidad de cambiar 60 créditos por 10 dias Plus(Sin bono de créditos)


        ✥ Paquete Créditos ✥

🜲 100/créditos = $4.50 USD 
🜲 200/créditos = $8.00 USD
🜲 250/créditos = $10.50 USD

        ✥ Rebajas Plus y Plus+ ✥

🜲 100/créditos = $3.50 USD 
🜲 200/créditos = $6.15 USD
🜲 300/créditos = $8.50 USD
        =================================|
        '''
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=precios_text,
        reply_markup=combined_keyboard,
        disable_web_page_preview=True,
        parse_mode="HTML"
    )

def register_callback_handlers(bot: TeleBot):
    bot.register_callback_query_handler(handle_back, func=lambda call: call.data == 'atras')
    bot.register_callback_query_handler(handle_opción1, func=lambda call: call.data == 'cuenta')
    bot.register_callback_query_handler(handle_opcion3, func=lambda call: call.data == 'tools')
    bot.register_callback_query_handler(handle_opcion4, func=lambda call: call.data == 'precios')
