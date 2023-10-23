from pyrogram.enums import ChatMemberStatus
import pyrogram 
async def does_joined(m,c):
    for ID in Var.FORCE_CHANNEL_ID:
        try :
            e = await c.get_chat_member(ID,m.from_user.id)
            if e.status == enums.ChatMemberStatus.BANNED :
                await m.reply(Var.BANNED)
            return
        except UserNotParticipant:
            await m.reply(Var.MUST_JOIN,reply_markup=JOIN_KEYBOARD)