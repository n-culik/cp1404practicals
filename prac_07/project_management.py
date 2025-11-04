"""
CP1404 Practical
Project management code to handle projects
Date: 04.11.2025
Author: Nicola Culik
Estimate: 300 min
Actual:   min
"""
from project import Project

MENU="""- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

def main():
    filename = "projects.txt"
    projects = open_file(filename)
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

def open_file(filename):
    """Open a file"""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            priority = int(parts[2])
            cost = float(parts[3])
            completion_percent = int(parts[4])
            project = Project(parts[0], parts[1], priority, cost, completion_percent)
            projects.append(project)
    return projects

main()