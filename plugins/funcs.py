async def is_number(number):
        try :
            int(number)
            return True 
        except ValueError :
            return False         