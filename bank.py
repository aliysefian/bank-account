import json
def deposit(user_data, amount, users_file):
    # Define a function to deposit money into the user's account

    user_data['balance'] += amount

    # Update the user's data in the file
    updated_users = []
    with open(users_file, 'r') as file:
        for line in file:
            data = json.loads(line)
            if data['national_id'] == user_data['national_id']:
                data['balance'] = user_data['balance']
            updated_users.append(data)

    # Write the updated data back to the file
    with open(users_file, 'w') as file:
        for data in updated_users:
            json.dump(data, file)
            file.write('\n')

def withdrawn(user_data, amount, users_file):
    """"""

    user_data['balance'] -= amount
    if  user_data['balance'] <0:
        print("You don't have enough money")
        return  

    # Update the user's data in the file
    updated_users = []
    with open(users_file, 'r') as file:
        for line in file:
            data = json.loads(line)
            if data['national_id'] == user_data['national_id']:
                data['balance'] = user_data['balance']
            updated_users.append(data)

    # Write the updated data back to the file
    with open(users_file, 'w') as file:
        for data in updated_users:
            json.dump(data, file)
            file.write('\n')