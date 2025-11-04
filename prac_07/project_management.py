"""
CP1404 Practical
Project management code to handle projects
Date: 04.11.2025
Author: Nicola Culik
Estimate: 300 min
Actual:   min
"""

MENU="""- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            break
        elif choice == "S":
            break
        elif choice == "D":
            break
        elif choice == "F":
            break
        elif choice == "A":
            break
        elif choice == "U":
            break
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")



main()