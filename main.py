from bank import deposit, withdrawn
from user import register_user, login_user
import json
import math


if __name__=="__main__":
    # Main program
    users_file = 'users.json'
    login_user_code = None
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Log In")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user(users_file)
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login_user_code,user_data = login_user(username, password, users_file)
            
            if login_user_code:
                print(f"Logged in with national ID: {login_user_code}")
                while True:
                    print("\nBanking Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Logout")
                    banking_choice = input("Enter your choice: ")
                    
                    if banking_choice == '1':
                        amount = float(input("Enter the deposit amount: "))
                        amount: float=abs(amount)
                        deposit(user_data=user_data,amount=amount, users_file=users_file)
                    elif banking_choice == '2':
                        amount = abs(float(input("Enter the withdrawal amount: ")))
                        # Implement withdrawal logic here
                        withdrawn(user_data,amount,users_file)
                    elif banking_choice == '3':
                        login_user_code = None
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Login failed. Username or password is incorrect.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
