
from pyrogram import Client as wase,filters,enums
from pyrogram.errors import *
from pyrogram.types import *
import asyncio
from helpers.buttons import *
from helpers.database import Database ,payment_db
from helpers.force_sub import does_joined, does_invited_joined
from plugins.funcs import is_number 
from helpers.custom_filters import filters_refferal , filters_film

@wase.on_message(filters.chat(Var.ALLOWED_CHATS) & filters.new_chat_members , group = 2)
async def user_adders(c,m):
    user_id = m.from_user.id
    name = m.from_user.first_name
    Db = Database(user_id)
    Db.approved_user(0.50)
    await c.send_message(user_id , '😊ሰላም {} 1 ሰው ወደ ግሩፓችን Add በማድረጎ 0.50 ብር አግኝተዋል።'.format(name))


@wase.on_message((filters.command(['faq']) | filters.regex('FAQ')))
async def faq_handler(c,m):
    await m.reply(Var.FAQS)

@wase.on_message(filters_refferal & filters.command(['start']))
async def refferal_handler(c,m):
    force = await does_invited_joined(c,m)
    if force == True:
        return 
    else :
        pass
    user_first_name = m.from_user.first_name
    user_id  = m.from_user.id
    Db = Database(user_id)
    _ , inviter_user_id = m.text.split(" ")
    inviter_user_id = int(inviter_user_id.replace('ref',''))
    if Db.user_exist() == True :
        await m.reply(Var.WELCOME.format(user_first_name) , reply_markup = Buttons.WELCOME_MARKUP)
        return
    else :
        pass 
    IDb = Database(inviter_user_id)
    IDb.approved_user(1)
    Db.approved_user(3)
    balance = IDb.usage()
    await c.send_message(inviter_user_id ,""" 🎉 በርሶ መጋበዣ ሊንክ 1 ሰው ተቀላቅሎል።

🧧ያገኙት የብር መጠን ~> 1 ብር።
🎁አሁን ያሎት ቀሪ ሂሳብ ~> {} ብር ነው።""".format(balance))
    
    await m.reply(Var.WELCOME.format(user_first_name) , reply_markup = Buttons.WELCOME_MARKUP)
         
 
@wase.on_message(filters_film & filters.command(['start']))
async def film_handler(c,m):
    force = await does_joined(c,m)
    if force == True:
        return 
    else :
        pass 
    user_id  = m.from_user.id
    try :
        Db = Database(user_id)
        points = Db.usage()
    except:
        await m.reply("""📮ይቅርታ ቦቱን አፕዴት አላረጉም ከመጠቀሞ በፊት /start በመላክ አፕዴት ያርጉ።
🔺update ለማረግ👇🏻
/start /start /start /start 
/start /start /start /start 
/start /start /start /start""")
        return
    if points < 2 :
        await m.reply(Var.NOT_ENOUGH)
        return
    else :
        pass 
    print(m.text)
    _ , called = m.text.split(" ")
    try:
        await c.copy_message(user_id ,-1001850882727 , int(called) , protect_content = True)
    except  Exception as e  :
        await c.send_message(689467742 , e)
        await m.reply('የቅርታ ይህ film ወደ ሌላ ዳታቤዝ ተዛውሯል ፤ ስሙን በድጋሚ በመፃፍ ወይም search በማድረግ ከ አዲሱ ዳታቤዛችን ሊያገኙት ይችላሉ ።')
        return 
    Db.purchased()
        

@wase.on_message(filters.private & filters.command(['start']))
async def start_message(c,m):
    force = await does_joined(c,m)
    if force == True:
        return 
    else :
        pass
    user_first_name = m.from_user.first_name
    user_id = m.from_user.id
    Db = Database(user_id)
    Db.approved_user(0)
    await m.reply('.' , reply_markup = Buttons.HELP_KEYBOARD)
    await m.reply(Var.WELCOME.format(user_first_name) , reply_markup = Buttons.WELCOME_MARKUP)
         
    

@wase.on_message(filters.private & (filters.command(['refferal'])  | filters.regex('🙌🏻 መጋበዣ ሊንክ')))
async def refferal_message(c,m):
    force = await does_joined(c,m)
    if force == True:
        return 
    else :
        pass 
    user_id = m.from_user.id
    link = Var.INVITATION_LINK.format(str(user_id))
    await m.reply("""🤷🏻‍♂ ይጋብዙ እና ነፃ የዋሴ ትርጉም ፊልሞችን ይኮምኩሙ!

🤳🏼 አንድ ሰው ሲጋብዙ 1 ብር ይሰራሉ ።

📮 መጋበዣ ሊንክ :~ {}""".format(link),reply_markup=None)
    
@wase.on_message(filters.private & (filters.command(['help'])  | filters.regex('🍁ማዘዣዎች🍁')))
async def help_message(c,m):
    await m.reply(Var.HELP_MESSAGE ,reply_markup=Buttons.HELP_MARKUP)

@wase.on_message(filters.private & (filters.command(['Balance'])|filters.regex('💵 ቀሪ ሂሳብ')))
async def balance_check(c,m):
    force = await does_joined(c,m)
    if force == True:
        return 
    else :
        pass 
    user_id  = m.from_user.id
    Db = Database(user_id)  
    points = Db.usage()
    await m.reply(Var.BALANCE_CHECK.format(points)) 


@wase.on_message(filters.private & filters.user(Var.OWNERS) & filters.command(['users']))
async def users_check(_,m):
    try :
        count = Database(1).users_count()
        await m.reply(f'you have {count} users')
    except Exception as e:
        await m.reply(e)

@wase.on_message(filters.private & filters.user(Var.OWNERS) & filters.command(['give']))
async def give_one(c,m):
    givaway = m.text.split(' ')
    Db = Database(int(givaway[-2]))
    try :
        Db.approved_user(int(givaway[-1]))
        await c.send_message(int(givaway[-2]),'👏🏼የብር ስጦታ ደርሶውታል ሂሳቦን ያረጋግጡ!')
        await m.reply('Done')
    except Exception as e :
        Db.throw_user()
        await m.reply(f'failed because \n\n{e}')

@wase.on_message(filters.private & filters.user(Var.OWNERS) & filters.command(['giveall']))
async def give_all(c,m):
    givaway = m.text.split(' ')
    for user in payment_db.find():
                        try :
                            Db = Database(user['user_id'])
                            Db.approved_user(int(givaway[-1]))
                            await c.send_message(user['user_id'],'👏🏼የብር ስጦታ ደርሶውታል ሂሳቦን ያረጋግጡ!')
                        except UserIsBlocked :
                            Db.throw_user()
                            pass
                        except InputUserDeactivated:
                            pass
                        except PeerIdInvalid:
                            pass
                        except FloodWait as e:
                            await asyncio.sleep(e.x)     
                        except UserIsBot :
                            pass 
                        except Exception as error:
                            await m.reply(error)
    await m.reply('Done')





