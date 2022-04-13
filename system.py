from lib.objects import *
from time import sleep


filename = 'users.txt'
while True:                 # Structuring the menu
    option = Menu.print_menu(
        ['List Users', 'Add a User', 'Exit Program'])   # Add menu options
    if option == 0:
        if not Database.file_exists(filename):
            Database.create_file(filename)
        Database.display_users(filename)
        
    elif option == 1: 
        if not Database.file_exists(filename):
            Database.create_file(filename)
        Menu.header('NEW SIGN UP')
        username = str(input('What is your name?'))
        age = str(input('Hou old are you?'))
        Database.sign_up(filename, username, age)
        
    elif option == 2:
        Menu.header('\033[35mGood Bye!\033[m')
        sleep(2)
        break

    else:                   # Validate Option
        Menu.header('\033[31mInvalid Option!\033[m') 
        sleep(2)