import Route
import Station
import User
import Database
"""
Created on Wed Dec 14 17:58:52 2016

@author: Bram
"""


class Main2():

    db = Database()
    
    def __init__(self):
        login = False
    
    def start(self):
        print("Welcome to our app.")
        logOrReg = input("Please type login or register.")
        if logOrReg == 'login':
            self.login()
        elif logOrReg == 'register':
            self.register()
        else:
            print('Maybe you made an error, please type login or register.')
        
    def login(self):
        mail = input("Mail: ")
        password = input("Password: ")
        
    def register(self):
        mail = input("Mail: ")
        password = input("Password: ")
        password = input("Repeat your password: ") 
        

a = Main()
a.start()