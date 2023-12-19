class Account_Type:
    def __init__(self, id, name, description):
        self.__id = id
        self.__name = name
        self.__description = description

    def __str__(self):
        return """Account Type ID: {}
        Account Type Name: {}
        Account Type Description: {}""".format(self.__id, self.__name, self.__description)