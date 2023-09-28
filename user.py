import json

# Define the User class
class User:
    def __init__(self, name, last_name, national_id, username, password):
        self.name = name
        self.last_name = last_name
        self.national_id = national_id
        self.username = username
        self.password = password
        self.balance = 0  # Initialize balance to zero

# Function to register a new user
def register_user(users_file):
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    national_id = input("Enter your national ID: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    user = User(name, last_name, national_id, username, password)
    
    with open(users_file, 'a') as file:
        json.dump(user.__dict__, file)
        file.write('\n')

# Function to log in a user
def login_user(username, password, users_file):
    with open(users_file, 'r') as file:
        for line in file:
            user_data = json.loads(line)
            if user_data['username'] == username and user_data['password'] == password:
                return user_data['national_id'],user_data
    return None

# Main program
users_file = 'users.json'
login_user_code = None

# while True:
#     print("\nMain Menu:")
#     print("1. Register")
#     print("2. Log In")
#     print("3. Exit")
#     choice = input("Enter your choice: ")

#     if choice == '1':
#         register_user(users_file)
#     elif choice == '2':
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         login_user_code = login_user(username, password, users_file)
        
#         if login_user_code:
#             print(f"Logged in with national ID: {login_user_code}")
#             while True:
#                 print("\nBanking Menu:")
#                 print("1. Deposit")
#                 print("2. Withdraw")
#                 print("3. Logout")
#                 banking_choice = input("Enter your choice: ")
                
#                 if banking_choice == '1':
#                     amount = float(input("Enter the deposit amount: "))
#                     # Implement deposit logic here
#                 elif banking_choice == '2':
#                     amount = float(input("Enter the withdrawal amount: "))
#                     # Implement withdrawal logic here
#                 elif banking_choice == '3':
#                     login_user_code = None
#                     break
#                 else:
#                     print("Invalid choice. Please try again.")
#         else:
#             print("Login failed. Username or password is incorrect.")
#     elif choice == '3':
#         break
#     else:
#         print("Invalid choice. Please try again.")
