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
    count_of_projects = count_projects(projects)

    print("Welcome to Pythonic Project Management")
    print(f"Loaded {count_of_projects} projects from {filename}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            break
        elif choice == "S":
            break
        elif choice == "D":
            display_projects(projects)
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
    write_file(filename, projects)
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

def count_projects(projects):
    """Count the number of projects in projects list"""
    count = 0
    for project in projects:
        count += 1
    return count

def display_projects(projects):
    """Display projects list"""
    completed_projects = []
    incomplete_projects = []

    for project in projects:
        if not project.is_complete():
            incomplete_projects.append(project)
        else:
            completed_projects.append(project)
    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(project)
    print("Completed projects: ")
    for project in completed_projects:
        print(project)

def write_file(filename, projects):
    """Write projects to a file"""
    with open(filename, "w") as out_file:
        out_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
        for project in projects:
            text_data = f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost}\t{project.completion_percent}\n"
            out_file.write(f"{text_data}")

main()