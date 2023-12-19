from Database import *
from Account_Type import *

if __name__ == '__main__':

    finances_db = Database()

    at = finances_db.get_account_types()
    account_types = []
    for t in at:
        account_types.append(Account_Type(t[0], t[1], t[2]))
    
    for account_type in account_types:
        print(account_type)

    finances_db.disconnect()