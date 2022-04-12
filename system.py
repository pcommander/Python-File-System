from lib.objects import *
from time import sleep



while True:                 # Structuring the menu
    option = Menu.print_menu(['List Users', 'Add a User', 'Create File', 'Exit Program'])   # Add menu options 
    if option == 0:
        Menu.header('Option 0')
        
    elif option == 1: 
        Menu.header('Option 1')
        
    elif option == 2:
        Menu.header('Option 2')
        
    elif option == 3:
        Menu.header('\033[35mGood Bye!\033[m')
        sleep(2)
        break

    else:                   # Validate Option
        Menu.header('\033[31mInvalid Option!\033[m') 
        sleep(2)