from pymongo import MongoClient
from config import Variables 
import dns.resolver

Var = Variables()
client = MongoClient(Var.MONGODB) 
db = client.database 
payment_db = db.paid_user
transaction_db = db.archive_transaction 
def before():
    collection = transaction_db.find_one({'transaction':'archive'})
    mk_list = (collection['transactions'])
    return mk_list
def archive_transactions(id):
    collection = transaction_db.find_one({'transaction':'archive'})
    mk_list = (collection['transactions'])
    mk_list.append(id)
    filt ={'transaction':'archive'}
    payload = {'$set':{'transactions':mk_list}}
    transaction_db.update_one(filt,payload)

class Database:
    def __init__(self , user_id):
        self.user_id = user_id
    def user_exist(self):
        existed = payment_db.find_one({'user_id':self.user_id})
        return True if existed else False
    def users_count(self):
        users = len(list(payment_db.find()))
        return users
    def usage(self):
        qoute = payment_db.find_one({'user_id':self.user_id})
        return qoute["points"]
    def approved_user(self,points):
        if Database(self.user_id).user_exist() == False:
            payload = {'user_id':self.user_id,'points':3}
            payment_db.insert_one(payload)
        else :
            old_point = Database(self.user_id).usage()
            filt ={'user_id':self.user_id}
            payload = {'$set':{'user_id':self.user_id ,'points':points+old_point}}
            payment_db.update_one(filt,payload)
    
    def purchased(self):
        points = Database(self.user_id).usage()
        filt ={'user_id':self.user_id}
        payload = {'$set':{'user_id':int(self.user_id) ,'points':points-2}}
        payment_db.update_one(filt,payload)
    def throw_user(self):
        filt ={'user_id':self.user_id}
        payment_db.delete_one(filt)
