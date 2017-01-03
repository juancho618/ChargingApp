__author__ = 'Jorge'
import re

def checkEmail(email):

    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    if match is None:
            print('Bad Syntax, please enter a valid email')
            return False
    else:
            return True


def passMatch(pass1, pass2):
    if pass1 == pass2:
        return True
    else:
        return False


def signUp():
    user = input("User: ")
    email = input("e-mail: ")
    while not checkEmail(email):
        email = input("e-mail: ")
    password = input("Password: ")
    password2 = input("Retype Password: ")
    while not passMatch(password,password2):
        password = input("Password: ")
        password2 = input("Retype Password: ")
        # adding user somehow with the methods of class user and Database
        # im not doing it yet thx though
    userMenu(user)


def userMenu(user):
    print(" Welcome %s" % user)
    print(" 1. makeReservation. ")
    print(" 2. checkMap. ")
    print(" 3. Logout. \n")
    try:
        optionUser = int(input("Please select an option: "))
    except ValueError:
        print("You have selected invalid option, please try again. ")


def printMenu():

    print(" Welcome to EVMApp,  Electric Vehicle charger station Map App ")
    print(" 1. Sign in. ")
    print(" 2. Sign up. ")
    print(" 3. Shut Down Interface. \n")


def program():

    noOption = True

    while noOption:
        printMenu()
        try:
                option = int(input("Please select an option: "))

                if option == 1:
                    print("option 1")
                    # signIn()

                elif option == 2:
                    print("option2")
                    signUp()

                elif option == 3:
                    print("exiting...")
                    noOption = False
                else:
                    print("Invalid Option. Please try again ")

        except ValueError:
                print("You have selected invalid option, please try again. ")

program()

