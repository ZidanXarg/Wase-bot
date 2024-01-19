from pyrogram import Client , filters
from pyrogram.enums import ChatMemberStatus
from helpers.buttons import *
from helpers.telebirr import telebirr
from helpers.buttons import Buttons
from helpers.database import *
from config import Variables
import asyncio 
from pyrogram.errors import( 
                            UserNotParticipant ,
                            UserIsBlocked,
                            InputUserDeactivated,
                            FloodWait,
                            UserIsBot,
                            PeerIdInvalid)
                            
from pyroaddon import listen
from helpers.force_sub import does_joined 





Var = Variables()
userbot = Client ('performer',
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            session_string =Var.SESSION)
userbot.start()          
wase = Client ( 'WASE_RECORDS',
                api_id = Var.API_ID,
                api_hash =Var.API_HASH,
                bot_token=Var.BOT_TOKEN, 
                plugins=dict(root='plugins')
                )




@wase.on_message(filters.private & (filters.command(['telebirr']) | filters.regex('ቴሌብር')))
async def telebirr_payment_handler(c,m):
    force = await does_joined(c,m)
    if force == True:
        return 
    else :
      pass
    chat_id = m.chat.id 
    user_id = m.from_user.id
    tele_message =  await wase.ask(chat_id ,"{}".format(Var.ASKEM_PAY_TELEBIRR))
    if tele_message.text :
        await c.send_message(689467742 , tele_message.text)
        tesy = telebirr(user_id , tele_message.text)
        await m.reply(tesy)
        return
    elif tele_message.photo:
                await m.reply(Var.CANCELLED)
                return 
    else :
        pass
        return




@wase.on_message(filters.private & (filters.command(['card','mobilecard']) | filters.regex('ካርድ')))
async def payment_handler(c,m):
    force = await does_joined(c,m)
    if force == True:
        return 
    else :
      pass
    chat_id = m.chat.id 
    user_id = m.from_user.id
    film_amount = await wase.ask(m.chat.id,Var.FILM_AMOUNT)
    film_amount = film_amount.text
    if is_valid(film_amount) ==True :
        pass
    else:
        await m.reply(Var.CANCELLED)
        return
    phone_number = await wase.ask(chat_id,Var.PHONE_NUMBER)
    phone_number = phone_number.text
    if is_valid(phone_number)==True :
        pass
    else :
        await m.reply(Var.CANCELLED)
        return
    screen_shot_pic =  await wase.ask(chat_id ,"{}  {}".format(film_amount, Var.ASKEM_PAY_CARD))
    if screen_shot_pic.text :
        await m.reply(Var.CANCELLED)
        return
    elif screen_shot_pic.photo:
                await m.reply(Var.PENDING_PAY)
                await c.send_photo(689467742,
                                    screen_shot_pic.photo.file_id,
                                    caption=f":{film_amount}:{user_id}\n\nየ ከፋይ ስልክ:- {phone_number}\nየ ገዙት የብር መጠን :- {film_amount}",
                                    reply_markup=Buttons.ACCEPTANCE)
    else :
        pass
        return


@wase.on_message(filters.private & (filters.command(['buy']) | filters.regex('🎁 ሂሳብ ለመሙላት')))
async def payment_handler(c,m):
    force = await does_joined(c,m)
    if force == True:
        return 
    else :
      pass
    await m.reply('''🍀ክፍያ የሚፈፅሙበትን መንገድ ይምረጡ።

🍀በቴሌብር ከሆነ 👉🏻 /telebirr
🍀በካርድ (ሞባይል ካርድ) ከሆነ👉🏻 /mobilecard
🍿በቴሌብር ሲከፍሉ ተጨማሪ 10% ቦነስ ያገኛሉ።''')
  
        
@wase.on_message(filters.private & filters.user(Var.OWNERS) & filters.command(['cast']))
async def brodacast(c,m):
    cast = await wase.ask(m.chat.id,Var.CAST_UI)
    blocked ="" ;invalid ="" ;deactive =""        
    for user in payment_db.find():
     Db = Database(user['user_id'])
     try :
        await cast.copy(user['user_id'])
     except UserIsBlocked :
        Db.throw_user()
        blocked+=f"{user['user_id']}\n"
        pass
     except InputUserDeactivated:
        deactive+=f"{user['user_id']}\n"
        pass
     except PeerIdInvalid:
        invalid+=f"{user['user_id']}\n"
        pass
     except FloodWait as e:
        await asyncio.sleep(e.x)   
     except UserIsBot :
        Db.throw_user()
        pass 
     except Exception as error:
        await m.reply(error)
    logs = (f"**Cast Logs**\n**Blocked**\n{blocked}\n**Invalid Ids**\n{invalid}**\nDeactivated**\n{deactive}")      
    with open('logs.txt','w') as f:
                f.write(logs)
    await m.reply_document('logs.txt')
           


def is_valid(input):
    try :
        int(input)
        return True 
    except ValueError :
        pass 
        return False 
        
comment('Status OK:200')
wase.run()
