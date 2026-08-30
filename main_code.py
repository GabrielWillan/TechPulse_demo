import time

wait = time.sleep

menu_str = "Welcome to Office101"
menu_choices_str = ("LogIn(1)\nSignUp(2)\nEXIT(3)\nSelect Input:")
global_choices = ("1", "2", "3")
max_char_len = 20
min_char_len = 3
signin_menu_str = "Account Creation"
login_menu_str = "LogIn menu"



def create_account():
    print(signin_menu_str)
    while True:
     username_input = input("Enter username:")
     if len(username_input) > max_char_len:
         print("Username too long")
         continue
     elif len(username_input) < min_char_len:
         print("Username too short")
         continue
     else:
         print("Username succesfully created")
         wait(1)
         break
     
    
    while True:
        password_input_first = input("Enter password:")
        if len(password_input_first) > max_char_len:
            print("Password too long")
        elif len(password_input_first) < min_char_len:
            print("Password too short")
        else:
            break

        

    while True:
        password_input_second= input("ReEnter password:")
        if password_input_second == password_input_first:
            completed_password = (password_input_second,password_input_first)
            print("Password succefully created")
            wait(2)
            print("Account succesfully created")
            break
        
        else:
            print("Password is invalid, please enter matching password! ")
        
    return{"username": username_input, "password":completed_password}
  
   
   
           
def login_accounts():
    print(login_menu_str)
    stored_accounts = office.accounts
    wait(2)
    while True:
        login_username_input = input("Enter Username:")
        login_password_input = input("Enter Password:")

        
        for accounts in stored_accounts:
            if login_username_input == accounts["username"] and login_password_input == accounts["password"]:
                print("Login worked")
                break
        else:
                print("invlaid, retry")
                continue

        
        


           
           
           
           
 




            

class the_office:
    def __init__(self):
        self.rules = []
        self.accounts = []

    def save_accounts(self, accounts):
        self.accounts.append(accounts)
    




office = the_office()





    
while True:
        print(menu_str)
        wait(2)
        menu_input = input(menu_choices_str)
        if menu_input in global_choices:
            if menu_input == global_choices[0]:
                login = login_accounts()
                wait(2)
                continue
            elif menu_input == global_choices[1]:
                account = create_account()
                office.save_accounts(account)
                continue
            else:
               print("EXIT")
               break
        else:
            print("invalid input")
            continue








