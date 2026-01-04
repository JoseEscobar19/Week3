def show_homepage():
    print("         ===DonateMe Homepage===         ")
    print("------------------------------------------")
    print("| 1.     Login      | 2.    Register     |")
    print("------------------------------------------")
    print("| 3.    Donate      | 4.  Show Donations |")
    print("------------------------------------------")
    print("|            5.     Exit                 |")
    print("------------------------------------------")

#task6, donate functionality

def donate(username):
    donation_amt = input("Enter amount to donate")
    donation_string = f"{username} donated ${donation_amt}"
    print(donation_string)
    print("thank you for your donation!")
    return donation_string

#task7, show donations functionality

def show_donations(donations):
    print("\n---All Donations---")
    if donations == []:
        print("there are currently no donations")
    else:
        for item in donations:
            print(item)
            
