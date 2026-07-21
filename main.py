#Main entry point for Network Utility Toolkit
#Displays the menu and routes the user to their desired tool
#running this 
from ping_tool import ping_host

def display_menu():
    print("===========================")
    print("  Network Utility Toolkit")
    print("===========================")
    print()
    print("Welcome!!")
    print()
    print("1. Ping Host")
    print("2. DNS Lookup")
    print("3. Port Scanner")
    print("4. Exit")
    print()

def dns_lookup():
    print("You selected DNS Lookup :)")
    print()

def port_scanner():
    print("You selected Port Scanner :)")
    print()

def exit_program():
    print("You have exited the program. Have a nice day :)")

#'while' function loops menu choice incase of errors and 'try' prevents error

#Asks user for input as well as displaying their choice back to them
while True:
    display_menu()
    try:
        menu_choice = int(input("Enter your choice here!!: "))
        print()

        if menu_choice == 1:
            ping_host()
        elif menu_choice == 2:
            dns_lookup()
        elif menu_choice == 3:
            port_scanner()
        elif menu_choice == 4:
            exit_program()
            break
        else:
            print()
            print("Please enter a valid input.")
            print()
    except ValueError:
        print()
        print("Please enter a numerical value.")
        print()
