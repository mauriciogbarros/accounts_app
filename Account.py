import datetime

class Account:
    def __init__(self, name = "", balance = 0, transactions = []):
        self.__name = name
        self.__balance = balance
        # transaction = (amount, date, category, subcategory, what, where, observations)
        self.__transactions = transactions

    # Getters
    def get_name(self):
        return self.__name
    
    def get_balance(self):
        return self.__balance
    
    # Setters
    def set_name(self, name = ""):
        if name != "":
            self.__name = name

    def set_balance(self, balance = 0):
        if balance != 0:
            self.__balance = balance

    # Adds
    def add_transactions(self, amount, date, category, subcategory, what, where, observations):
        # Add necessary checks
        self.__transactions.append((amount, date, category, subcategory, what, where, observations))
    
    # Updates
    def update_balance(self, amount = 0):
        self.__balance += amount