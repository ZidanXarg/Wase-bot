from pyrogram import filters
import pyrogram 



async def invite_filter(_,__,u):
    try :
        rc_data = u.text.split(" ")
    except:
        return False
    if len(rc_data)==2 and rc_data[1].startswith("ref") :
        return True 
    else :
        return False 
filters_refferal = filters.create(invite_filter)


 
async def films_filter(_,__,u):
    try :
        rc_data = u.text.split(" ")
    except:
        return False
    if len(rc_data) == 2 :
        return True 
    else :
        return False 
filters_film = filters.create(films_filter)


