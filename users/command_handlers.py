import requests, time, random
from telebot import TeleBot, types
from users.callback_handlers import create_main_keyboard
from config.bot_config import bot, BOT_NAME
from tools.card_gen import generate_card
from helpers.bin_info import get_bin_info
from helpers.fake_data import get_fake_data
from database.get_credits import get_credits
from database.get_rango import get_rango
from database.add_user import add_user
from helpers.user_exist import user_exist

# VARIABLE GLOBAL ####################
chat_id = None
# Manejador /start
@bot.message_handler(commands=['start'])
def start(message):
    global chat_id
    chat_id = message.chat.id
    username = message.from_user.username
    bot.send_message(message.chat.id, f'''=========================|
            🤖 {BOT_NAME} 🤖
         
            Si tienes algún problema o
            necesitas ayuda no dudes en
            contactar a mi programador😃
         
            By: <a href="https://t.me/alltallr">@Altaïr</a>
            =========================|
            ''', disable_web_page_preview=True, parse_mode="HTML", reply_markup=create_main_keyboard())
    time.sleep(1.5)
    if not user_exist(chat_id):
       add_user(chat_id, username)

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_chat_action(message.chat.id, 'typing')
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        user = message.from_user
    chat_id = message.chat.id
    user_info = f"""
    ===============================|
    🤖 INFORMACIÓN DE USUARIO 🤖
    🆔 ID: {user.id}
    👤 Usuario: @{user.username}
    🏅 Nombre: {user.first_name}
    💵 Créditos: {get_credits(chat_id)}
    👑 Rango: {get_rango(chat_id)}
    💻 CMDS: /info, /gen, /bin
    ===============================|
    """
    bot.reply_to(message, user_info, parse_mode="Markdown")

@bot.message_handler(commands=['cmds'])
def cmd(message):
    cmd_text=f'''======================|
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
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, cmd_text, parse_mode='Markdown')

# Comando para obtener información del BIN
@bot.message_handler(commands=['bin'])
def bin(message):
    bot.send_chat_action(message.chat.id, 'typing')
    # Obtener el BIN del mensaje del usuario
    bin_number = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if bin_number:
        try:
            bin_data = get_bin_info(bin_number)
            
            # Verifica si bin_data contiene la información necesaria
            if not bin_data:
                bot.reply_to(message, "ℹ️No se pudo obtener información del BIN. Intenta con otro.ℹ️")
                return
            # Construir el mensaje de respuesta con la información del BIN
            response_message = f"🤖Información del BIN {bin_number}:🤖\n\n"
            response_message += f"🌎País: {bin_data['country']['name']}\n"
            response_message += f"🌐Código de país: {bin_data['country']['alpha2']}\n"
            response_message += f"🪙Moneda: {bin_data['country']['currency']}\n"
            response_message += f"🏦Banco emisor: {bin_data['bank']['name']}\n"
            response_message += f"💳Tipo de tarjeta: {bin_data['type']}\n"
            response_message += f"〽️Marca: {bin_data['scheme']}\n"
            response_message += f"📈Nivel: {bin_data['brand']}"
            
            bot.reply_to(message, response_message)
        except Exception as e:
            bot.reply_to(message, f"⛔️Error al obtener información del BIN: {str(e)}⛔️")
    else:
        bot.reply_to(message, "ℹ️Por favor, proporciona un número BIN válido.ℹ️")

@bot.message_handler(commands=['countries'])
def bin_countrys(message):
    bot.send_chat_action(message.chat.id, 'typing')
    if not range == 'Free' or 'Premium' or 'Admin' or 'Dev':
        bot.reply_to(message, "🚫ACCESO A USUARIOS BAN NO PERMITIDOS🚫")
    edit1 = bot.reply_to(message, "<b>☇ Obteniendo Lista de Paises PREMIUM ...</b>")
    
    # Simulando un tiempo de espera
    bot.edit_message_text(chat_id=message.chat.id, message_id=edit1.message_id, text="Lista de países obtenida.")

    bot.edit_message_text(chat_id=message.chat.id, message_id=edit1.message_id, text="""
    𝑻𝒊𝒆𝒏𝒆𝒔 𝒂 𝒕𝒖 𝒅𝒊𝒔𝒑𝒐𝒔𝒊𝒄𝒊𝒐𝒏 𝒖𝒏𝒂 𝒆𝒙𝒕𝒆𝒏𝒔𝒂 𝒍𝒊𝒔𝒕𝒂 𝒅𝒆 𝒍𝒐𝒔 𝒔𝒊𝒈𝒖𝒊𝒆𝒏𝒕𝒆𝒔 𝒑𝒂𝒊𝒔𝒆𝒔 𝒒𝒖𝒆 𝒑𝒖𝒆𝒅𝒆𝒔 𝒈𝒆𝒏𝒆𝒓𝒂𝒓 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒄𝒊𝒐𝒏 𝒇𝒂𝒌𝒆:
    <b>COMANDO ⬌ CODE ⬌ COUNTRY 
    <code>/rand AU </code>⬌ AUSTRALIA 
    <code>/rand BR </code>⬌ BRASIL
    <code>/rand CA </code> ⬌ CANADA
    <code>/rand CH </code>⬌ SUIZA 
    <code>/rand DE </code>⬌ ALEMANIA (GERMANY)
    <code>/rand DK </code>⬌ DINAMARCA 
    <code>/rand ES </code>⬌ ESPAÑA (SPAIN)
    <code>/rand FI </code>⬌ FINDLANDIA
    <code>/rand FR </code>⬌ FRANCIA 
    <code>/rand GB </code>⬌ REINO UNIDO 
    <code>/rand IE </code>⬌  IRLANDA
    <code>/rand IN </code>⬌  INDIA
    <code>/rand IR </code>⬌  IRAN
    <code>/rand MX </code>⬌ MEXICO 
    <code>/rand NL </code>⬌ NETHERLANDS
    <code>/rand NO </code>⬌ NORWAY
    <code>/rand NZ </code>⬌ HAMILTON
    <code>/rand RS </code>⬌ SERVIA
    <code>/rand TR </code>⬌ TURQUIA
    <code>/rand UA </code>⬌ UKRANIA
    <code>/rand US </code>⬌ ESTADOS UNIDOS
    Genera datos fake con: comando + el pais seleccionado.</b>
    <code>/infake US</code>
    """)

@bot.message_handler(commands=['rand'])
def bin_rand(message):
    bot.send_chat_action(message.chat.id, 'typing')
    if not range == 'Free' or 'Premium' or 'Admin' or 'Dev':
        bot.reply_to(message, "🚫ACCESO A USUARIOS BAN NO PERMITIDOS🚫")
    infake = message.text[len("/rand"):].strip().upper()  # Convertir a mayúsculas para el código de país

    if not infake:
        return bot.reply_to(message, "Por favor, proporciona un código de país válido.")

    edit1 = bot.reply_to(message, "<b>☯ Generando Datos Fake Premium...</b>")
    
    infake_api = get_fake_data(infake)

    # Extracción de datos
    try:
        name = infake_api["results"][0]["name"]
        gender = infake_api["results"][0]["gender"]
        age = infake_api["results"][0]["dob"]["age"]
        birthdate = infake_api["results"][0]["dob"]["date"]
        street = infake_api["results"][0]["location"]["street"]['number']
        street1 = infake_api["results"][0]["location"]["street"]['name']
        city = infake_api["results"][0]["location"]["city"]
        state = infake_api["results"][0]["location"]["state"]
        postal = infake_api["results"][0]["location"]["postcode"]
        email = infake_api["results"][0]["email"]
        country = infake_api["results"][0]["location"]["country"]

        bot.edit_message_text(chat_id=message.chat.id, message_id=edit1.message_id, text=f"""
        𝐃𝐀𝐓𝐎𝐒 𝐅𝐀𝐊𝐄 𝐏𝐑𝐄𝐌𝐈𝐔𝐌
        ⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊<b>
        ┌Name : <code>{name['first']} {name['last']}</code>
        ┝Gender :<code> {gender}</code>
        ┝Age :<code> {age}</code>
        ┝Birthdate :<code> {birthdate}</code>
        ┝Country :<code> {country}</code>
        ┝Street :<code> {street}- {street1}</code>
        ┝City :<code> {city}</code>
        ┝State : <code>{state}</code>
        ┝Postal Code :<code> {postal}</code>
        └Email :<code> {email}</code></b>
        ⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊
        """)
    except (IndexError, KeyError) as e:
        bot.edit_message_text(chat_id=message.chat.id, message_id=edit1.message_id, text="Error al obtener datos. Asegúrate de que el país sea válido.")

@bot.message_handler(commands=['extra'])
def extra(message):
    bot.send_chat_action(message.chat.id, 'typing')
    inputm = message.text.split(None, 1)[1]
    bincode = 6
    BIN = inputm[:bincode]
    yo = BIN[0:9]
    que = yo

    req = requests.get(
                    f"https://bins.antipublic.cc/bins/{BIN}").json()
                # capturas
    brand = req['brand']
    country_name = req['country_name']
    country_flag = req['country_flag']
    country_currencies = req['country_currencies']
    bank = req['bank']
    level = req['level']
    typea = req['type']
    que = BIN   
    #-----------FUNCION GNERADOR----------#
    hola0 = (random.randint(2024, 2030))
    hola1 = (random.randint(2024, 2030))
    hola2 = (random.randint(2024, 2030))
    hola3 = (random.randint(2024, 2030))
    hola4 = (random.randint(2024, 2030))
    hola5 = (random.randint(2024, 2030))
    hola6 = (random.randint(2024, 2030))
    hola7 = (random.randint(2024, 2030))
    hola8 = (random.randint(2024, 2030))
    hola9 = (random.randint(2024, 2030))
    si0 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si1 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si2 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si3 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si4 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si5 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si6 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si7 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si8 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    si9 = (random.choice(("01", "02", "03", "04", "05",
                       "06", "07", "09", "09", "10", "11", "12")))
    
    

    extra0 = (random.randrange(100000, 950000, 3))
    extra9 = (random.randrange(100000, 950000, 3))
    extra1 = (random.randrange(100000, 950000, 3))
    extra2 = (random.randrange(100000, 950000, 3))
    extra3 = (random.randrange(100000, 950000, 3))
    extra4 = (random.randrange(100000, 950000, 3))
    extra5 = (random.randrange(100000, 950000, 3))
    #--------PLANTILLA--------#

    message.reply(f"""<b>
**BIn: <code>{BIN}</code>**            
**Banco: <code>{bank}</code>**
**Pais: <code>{country_name}</code>**
**Datos: <code>{brand}-{typea}-{level}</code>**
**◈ ━━━━━━━ ⸙ ━━━━━━━ ◈**
**<code>{que}{extra0}xxxx|{si0}|{hola0}|rnd</code>**
**<code>{que}{extra9}xxxx|{si1}|{hola1}|rnd</code>**
**<code>{que}{extra1}xxxx|{si2}|{hola2}|rnd</code>**
**<code>{que}{extra2}xxxx|{si3}|{hola3}|rnd</code>**
**<code>{que}{extra3}xxxx|{si4}|{hola4}|rnd</code>**
**<code>{que}{extra4}xxxx|{si5}|{hola5}|rnd</code>**
**<code>{que}{extra5}xxxx|{si6}|{hola6}|rnd</code>**
◈ ━━━━━━━ ⸙ ━━━━━━━ ◈
""")

@bot.message_handler(commands=['gen'])
def gen(message: types.Message):
    bot.send_chat_action(message.chat.id, 'typing')
    """Genera y envía las tarjetas al usuario."""
    bot.send_chat_action(message.chat.id, 'typing')
    
    args = message.text.split()
    if len(args) < 2:
        return bot.reply_to(message, "ℹ️Por favor proporciona un BIN. Ejemplo: /gen 445100ℹ️")
    
    bin_number = args[1]
    
    if not bin_number.isdigit() or len(bin_number) < 6:
        return bot.reply_to(message, "⛔️El BIN debe ser un número válido de al menos 6 dígitos.⛔️")
    
    cards = []
    for _ in range(10):
        card = generate_card(bin_number)
        mm = random.randint(1, 12)
        yy = random.randint(2023, 2028)
        cvv = random.randint(100, 999)
        cards.append(f"{card}|{mm:02}|{yy}|{cvv}")

    # Obtiene información del BIN
    bin_info = get_bin_info(bin_number)
    
    # Prepara la respuesta
    response = f"✅Se han generado 10 tarjetas a partir del BIN `{bin_number}`:✅\n"
    response += f"• 🧾: {bin_number}\n"
    response += f"• 🔝: {bin_info['brand']}|{bin_info['type']}\n"
    response += f"• 🏛: {bin_info['bank']}\n"
    response += f"• 🌎: {bin_info['country']}\n"
    response += "━━━━━ 💳 ━━━━━\n"
    
    for card in cards:
        response += f"{card}\n"
    
    bot.reply_to(message, response, parse_mode="Markdown")

def register_command_handlers(bot: TeleBot):
    bot.register_message_handler(start, commands=['start'])
    bot.register_message_handler(info, commands=['info'])
    bot.register_message_handler(start, commands=['çountries'])
    bot.register_message_handler(start, ['rand'])
    bot.register_message_handler(start, ['extra'])
    bot.register_message_handler(start, commands=['bin'])
    bot.register_message_handler(start, commands=['gen'])
    bot.register_message_handler(start, commands=['cmds'])