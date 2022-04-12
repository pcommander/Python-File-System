class User:
    def __init__(self):
        self.name = str(input('What is your name?'))
        self.age = int(input('How old are you?'))


class Database:
    """
    Methods for manipulating the .txt files. 
    """
    def __init__(self):
        pass

    def open_txt():
        pass

    def sign_up():
        pass

    def display_data():
        pass

    def clear_database():
        pass 


class Menu:
    """
    Methods for structuring and designing our app's menu.
    """
    def __init__(self):
        pass

    def read_int(msg):
        while True:
            try:
                number = int(input(msg))
            except (ValueError, TypeError, KeyboardInterrupt):
                print('\033[31mInvalid input, integer expected!\033[m')
                continue
            else:
                return number
    def line(size=42):
        return '-' * size

    def header(txt):
        print(Menu.line())
        print(txt.center(42))
        print(Menu.line())
    
    def print_menu(list):
        Menu.header('MAIN MENU')
        for i, c in enumerate(list):
            print(f'\033[33m{i}\033[m for: \033[34m{c}\033[m')
        print(Menu.line())
        option = Menu.read_int('\033[32mYour Option:\033[m')
        return option
