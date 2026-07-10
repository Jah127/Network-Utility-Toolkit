#Main entry point for Network Utility Toolkit
#Displays the menu and routes the user to their desired tool

print("===========================")
print("Network Utility Toolkit")
print("===========================")
print()
print("Welcome!!")
print()
print("1. Ping Host")
print("2. DNS Lookup")
print("3. Port Scanner")
print("4. Exit")
print()

where = float(input())

if where == 1:
    print("You selected Ping Host :)")
elif where == 2:
    print("You selected DNS Lookup :)")
elif where == 3:
    print("You selected Port Scanner :)")
else:
    print("You have exited the program :)")
