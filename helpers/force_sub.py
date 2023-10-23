from pyrogram.enums import ChatMemberStatus
import pyrogram 
from pyrogram.types import *
from config import Variables
from helpers.buttons import Buttons
from pyrogram.errors import UserNotParticipant
Var = Variables()

async def does_joined(c,m):
    for ID in Var.FORCE_CHANNEL_ID:
        fchat = m.chat.id
        if str(fchat).startswith('-100'):
            pass
        else :
            try :
                e = await c.get_chat_member(ID,m.chat.id)
                if e.status == ChatMemberStatus.BANNED :
                    await m.reply(Var.BANNED)
                    return False 
            except UserNotParticipant:
                await m.reply(Var.MUST_JOIN,reply_markup=Buttons.FORCE_MARKUP)
                return True 
async def does_invited_joined(c,m):
    for ID in Var.FORCE_CHANNEL_ID:
        try :
            e = await c.get_chat_member(ID,m.from_user.id)
            if e.status == ChatMemberStatus.BANNED :
                await m.reply(Var.BANNED)
            return False 
        except UserNotParticipant:
            BFI = Buttons.FORCE_INVITED
            refr = m.text.split(" ")
            if len(BFI) < 2:
                invite = [InlineKeyboardButton("😊ተቀላቅያለው",url=Var.INVITATION_LINK.format(refr[-1].replace('ref','')))]
                BFI.append(invite)
            
            else :
                invite = [InlineKeyboardButton("😊ተቀላቅያለው",url=Var.INVITATION_LINK.format(refr[-1].replace('ref','')))]
                BFI[1] = invite 
            await m.reply(Var.MUST_JOIN_INVITED,reply_markup=InlineKeyboardMarkup(Buttons.FORCE_INVITED))
            return True 
    




