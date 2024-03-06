from pyrogram import Client as wase ,filters,enums
from config import Variables 
from helpers.buttons import Buttons
from helpers.database import Database 
from pyrogram.types import *
from pyrogram.errors import *
from helpers.force_sub import does_joined 



Var = Variables()
userbot = wase ('performer',
            api_id=Var.API_ID,
            api_hash=Var.API_HASH,
            session_string =Var.SESSION) 
file_ids = {}
@wase.on_message((filters.group & filters.command(['search'])) | (filters.private & filters.text))
async def text_handler(c,m):
    force = await does_joined(c,m)
    if force == True:
        return 
    else :
        pass 
    user_id = m.chat.id
    try:
                first_name = m.from_user.first_name 
                user_name = m.from_user.username 
                await  c.send_message(Var.LOG_CHANNEL,'Search : {}\nUser ID : {}\nUsername : {}\nName : {}'.format(query ,user_id, user_name , first_name))       
    except :
                pass
    query = m.text.replace('/search','')
    if len(query) < 2 :
                await m.reply("የቅርታ የ ፊልም ስም አልሰጡኝም ☹️")
                return 
    else :
                pass
    file_ids[str(user_id)] = {}
    try :
        await userbot.start()
    except:
        pass
    await m.reply(Var.SEARCH_PENDING)
    async for message in userbot.search_messages(Var.FILM_SOURCE_CHANNEL,query):
        e = await c.get_messages(Var.FILM_SOURCE_CHANNEL,message.id)
        if e.document:
                    file_ids[str(user_id)][str(e.id)]=[e.document.file_name,e.document.file_id]
        elif e.video :
                    file_ids[str(user_id)][str(e.id)]=[e.video.file_name,e.video.file_id]
        else :
                    pass 
   
    try:
        await m.reply(query ,reply_markup=InlineKeyboardMarkup(
                                                                Buttons.film_selection(file_ids[str(user_id)])[0] 
                                                                ) , quote = True
                                                                )
    except IndexError :
        await m.reply(Var.RESULT_NOT_FOUND , quote = True )
        
        
@wase.on_callback_query() 
async def callback_func(c,u):
    user_id =u.from_user.id
    if u.data == 'approved':
        user = u.message.caption.splitlines()[0].split(':')[-1]
        tokens = u.message.caption.splitlines()[0].split(':')[-2]
        Db = Database(int(user))
        Db.approved_user(int(tokens))
        await u.message.edit(Var.YOU_APPROVED_IT)
        await c.send_message(user,Var.SUCCESS_PAYMENT)
    elif u.data == 'faq':
        await u.message.edit(Var.FAQS)
    elif u.data == 'help':
        await u.message.edit(Var.HELP_MESSAGE)            
    elif u.data == 'instruct' :
        await u.message.edit(Var.INSTRUCTION)
    elif u.data == 'denied':
        user = u.message.caption.splitlines()[0].split(':')[-1]
        await u.message.edit(Var.YOU_DECLINED_IT)
        await c.send_message(user,Var.FAILED_PAYMENT)
    elif u.data.startswith("tpage+"):
        page_no = int(u.data.split("+")[1]) - 1
        try :
                    await u.message.edit_reply_markup(
            InlineKeyboardMarkup(
                Buttons.film_selection(file_ids[str(user_id)])[page_no]))
        except :
                    pass
         
    else :
        await u.answer('ይህን film ማስታወስ አልቻልኩም😑፤ እስቲ አንዴ ደግመው የፃፉልኝ😊',show_alert=True)         
 
