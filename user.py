
#task4: Login functionality

def login(database, username, password):
    if username in database and database[username] == password:
        print(f"Welcome back {username}!")
    elif username in database and database[username] != password:
        print("Password incorrect")
        return ""
    else:
        print("Username not found")
        return ""