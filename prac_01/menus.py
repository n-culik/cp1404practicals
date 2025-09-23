"""
CP1404 Practical
In this program a menu will be displayed and the user can decide what to do.
It ends when the Quit option is selected
"""

MENU = """(H)ello
(G)oodbye
(Q)uit"""

user_name = input("Enter name: ")
print(MENU)
user_choice = input(">>>").upper()

# Loop as loog as the user did not type in q
while user_choice != "Q":
    # Decision-making based on the input of the user
    if user_choice == "H":
        print(f"Hello {user_name}")
    elif user_choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid choice")
    print(MENU)
    user_choice = input(">>> ").upper()
print("Finished.")