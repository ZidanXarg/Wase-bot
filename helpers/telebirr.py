#payment verfication programmed by NextDevil
import requests , json
from config import Variables 
from helpers.database import before , Database, archive_transactions as archv
def telebirr(user_id, text):
    Db = Database(user_id)
    Var = Variables()
    bef = before()
    if len(text) == 10 and text.isupper() :
        tran = text
        pass
    else :
        if  Var.TELEBIRR_PHONE not in text :
            return ('~ክፍያው ለኛ የተፈከፈለ አደለም❗️')
        else :
            pass
        raw = text.split('http')[1].split('/')[-1].split()
        for id in raw :
            if id.isupper() and len(id)==10:
                tran = id.replace('.','')
    if tran in bef:
        return ("~በዚ ሚሴጅ ከዚ በፊት ክፍያ ፈፅመውበታል❗️")
    requests.get('http://tele-birr-api.vercel.app/')  
    requests.get('http://tele-birr-api.vercel.app/?receipt=AII1QBLCTR')
    r = requests.get('http://tele-birr-api.vercel.app/?receipt={}'.format(tran))
    p = json.loads(r.text)
    if p['status']==True :
        receiver = p['receiver_number']
        date = p['date']
        d , m , y = date.split('-')
        x  = (int(d) >=17 and int(m) >= 9 and int(y) >=2023) 
        f = (int(d) <17 and int(m) <= 9 and int(y) >= 2023) 
        t = (int(d) <17 and int(m) >= 9 and int(y) >= 2023) 
        if x or f or t:
            pass
        else :
            return('the payment is old')
        if Var.TELEBIRR_PHONE in receiver:
            archv(tran)
            amount = int(float(p['total_amount'].replace('Birr','')))
            bonus = amount*(10/100)
            Db.approved_user(amount+bonus)
            return ('🎉ክፍያውን በተሳካ ሁኔታ ከፍለዋል ፤ እባኮ ቀሪ ሂሳቦን ያረጋግጡ።')
        else :
            return ('~ክፍያው ለኛ የተፈከፈለ አደለም❗️')
    elif p['status']== False :
         return ('~በዚ ሚሴጅ ምንም የተፈፀመ ክፍያ የለም❗️')
         
         
         








