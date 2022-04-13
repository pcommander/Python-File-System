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

    def file_exists(name):
        try:
            a = open(name, 'rt')
            a.close()
        except (FileNotFoundError):
            return False
        else:
            return True

    def create_file(name):
        try: 
            a = open(name, 'wt+')
            a.close()
        except:
            print('The file was not created due to an Error.')
        else:
            Menu.header("File was created successfully.")

    def sign_up(filename, username, age):
        try:
            a = open(filename, 'at')
        except:
            print('Error while opening file!')
        else:
            try:
                a.write(f'{username}; {age} \n')
            except:
                print('Error trying to store data')
            else:
                print('User Registered Successfully!')
                
    def display_users(name):
        try:
            a = open(name, 'rt')
        except:
            print('Error occurred when opening the file!')
        else:
            Menu.header('REGISTERED USERS')
            for line in a:
                data = line.split(';')
                data[1] = data[1].replace('\n', '')
                print(f'{data[0]:<30} {data[1]:>3} anos')
        finally:
            a.close()

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
