from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}

donations = []

authorized_user = ""

# show_homepage()

# if authorized_user == "":
#     print("you must be logged in to donate")
# else:
#     print(f"Logged in as: {authorized_user}")

#task 3, hanle user input

while True:
    show_homepage()

    if authorized_user == "":
        print("you must be logged in to donate")
    else:
        print(f"Logged in as: {authorized_user}")

    user_input = input("Choose an option: ")
#task 4,5,6,7 functionality

    if user_input == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)

    elif user_input == "2":
        username = input("Enter username")
        password = input("Enter password")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
            print(database)

    elif user_input == "3":
        if authorized_user == "":
            print("you are not logged in")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
            print(donations)

    elif user_input == "4":
        show_donations(donations)
        print(donations)
        
    elif user_input == "5":
        print("Goodbye! ")
        break
