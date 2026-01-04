from donations_pkg.homepage import show_homepage
from donations_pkg.user import login

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
        print("TODO: Writ5e Register functionality")
    elif user_input == "3":
        print("TODO: Writ5e Donate functionality")
    elif user_input == "4":
        print("TODO: Writ5e Show Donation functionality")
    elif user_input == "5":
        print("Goodbye! ")
        break