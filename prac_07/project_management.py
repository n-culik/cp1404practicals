"""
CP1404 Practical
Project management code to handle projects
Date: 04.11.2025
Author: Nicola Culik
Estimate: 300 min
Actual:   min
"""
import datetime
from project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
PROJECT_NUMBER_MENU = "Project choice: "
PROJECT_PERCENTAGE_MENU = "New Percentage: "
PROJECT_PRIORITY_MENU = "New Priority: "

def main():
    """Main function for menu and call other functions"""
    filename = "projects.txt"
    projects = open_file(filename)
    count_of_projects = count_projects(projects)

    print("Welcome to Pythonic Project Management")
    print(f"Loaded {count_of_projects} projects from {filename}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            user_file = input("Enter file name to load projects from: ")
            projects = open_file(user_file)
            count_of_projects = count_projects(projects)
            print(f"Loaded {count_of_projects} projects from {user_file}")
        elif choice == "S":
            user_file = input("Enter file name to save projects to: ")
            write_file(user_file, projects)
            count_of_projects = count_projects(projects)
            print(f"Saved {count_of_projects} projects to {user_file}")
        elif choice == "D":
            display_sorted_projects(projects)
        elif choice == "F":
            start_date = validate_date("Show projects that start after date (dd/mm/yyyy):")
            for project in projects:
                if project.start_date > start_date:
                    print(project)
        elif choice == "A":
            print("Let's add a new project")
            name = input("Name: ")
            start_date = validate_date("Start date (dd/mm/yy): ")
            priority = validate_priority_input("Priority: ")
            if priority == "":
                priority = 0
            cost = validate_float_input("Cost estimate: $")
            percentage = validate_percentage_input("Percent complete: ")
            if percentage == "":
                percentage = 0
            projects.append(Project(name, start_date, priority, cost, percentage))
        elif choice == "U":
            display_projects(projects)
            update_project_number = validate_project_numer(projects)
            print(projects[update_project_number])
            new_percentage = validate_percentage_input(PROJECT_PERCENTAGE_MENU)
            if new_percentage == "":
                new_percentage = projects[update_project_number].completion_percent
            new_priority = validate_priority_input(PROJECT_PRIORITY_MENU)
            if new_priority == "":
                new_priority = projects[update_project_number].priority
            projects = update_project(projects, update_project_number, new_percentage, new_priority)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    user_input = input(f"Would you like to save to {filename}?").upper()
    if user_input == "Y" or user_input == "YES" or user_input == "":
        write_file(filename, projects)
    else:
        filename = input("Enter file name to save projects to: ")
        write_file(filename, projects)
    print("Thank you for using custom-built project management software.")

def open_file(filename):
    """Open a file"""
    projects = []
    try:
        with open(filename, "r") as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.strip().split('\t')
                date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
                priority = int(parts[2])
                cost = float(parts[3])
                completion_percent = int(parts[4])
                project = Project(parts[0], date, priority, cost, completion_percent)
                projects.append(project)
    except FileNotFoundError:
        print(f"File {filename} not found")
    return projects

def count_projects(projects):
    """Count the number of projects in projects list"""
    count = 0
    for project in projects:
        count += 1
    return count

def display_projects(projects):
    """Display projects list"""
    index = 0
    for project in projects:
        print(f"{index} {project}")
        index += 1

def display_sorted_projects(projects):
    """Display sorted projects list"""
    completed_projects = []
    incomplete_projects = []

    for project in projects:
        if not project.is_complete():
            incomplete_projects.append(project)
        else:
            completed_projects.append(project)

    incomplete_projects.sort()
    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(project)

    completed_projects.sort()
    print("Completed projects: ")
    for project in completed_projects:
        print(project)

def validate_project_numer(projects):
    """Validate project number"""
    project_to_update = validate_project_number_input(PROJECT_NUMBER_MENU)
    is_valid = False
    while not is_valid:
        try:
            projects[project_to_update]
            is_valid = True
        except IndexError:
            print("Invalid project number")
            project_to_update = validate_project_number_input(PROJECT_NUMBER_MENU)
    return project_to_update

def validate_project_number_input(title):
    """Validates the user input for project number"""
    is_valid = False
    while not is_valid:
        try:
            user_input = int(input(f"{title}"))
            while user_input < 0:
                print("Number must be >= 0")
                user_input = int(input(f"{title}"))
            is_valid = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return user_input

def validate_percentage_input(title):
    """Validates the user input for percentage"""
    user_input = input(f"{title}")
    if user_input == "":
        return user_input
    else:
        is_valid = False
        while not is_valid:
            try:
                user_input = int(user_input)
                while user_input < 0 or user_input > 100:
                    print("Number must be between 0 and 100")
                    user_input = int(input(f"{title}"))
                is_valid = True
            except ValueError:
                print("Invalid input - please enter a valid number")
                user_input = input(f"{title}")
        return user_input

def validate_priority_input(title):
    """Validates the user input for priority"""
    user_input = input(f"{title}")
    if user_input == "":
        return user_input
    else:
        is_valid = False
        while not is_valid:
            try:
                user_input = int(user_input)
                while user_input < 1:
                    print("Number must be > 0")
                    user_input = int(input(f"{title}"))
                is_valid = True
            except ValueError:
                print("Invalid input - please enter a valid number")
                user_input = input(f"{title}")
        return user_input

def validate_float_input(title):
    """Validates the user input for cost"""
    is_valid = False
    while not is_valid:
        try:
            user_input = float(input(f"{title}"))
            while user_input < 0:
                print("Number must be >= 0")
                user_input = float(input(f"{title}"))
            is_valid = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return user_input

def validate_date(title):
    """Validate user input date"""
    is_valid = False
    while not is_valid:
        try:
            date_string = input(title)
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid = True
        except:
            print("Please enter date in (dd/mm/yyyy)")
    return date

def update_project(projects, update_project_number, new_percentage, new_priority):
    """Update project in projects list with given parameters"""
    project = projects[update_project_number]
    project.completion_percent = new_percentage
    project.priority = new_priority
    return projects

def write_file(filename, projects):
    """Write projects to a file"""
    with open(filename, "w") as out_file:
        out_file.write("Name	Start Date	Priority	Cost Estimate	Completion Percentage\n")
        for project in projects:
            text_data = f"{project.name}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t{project.cost}\t{project.completion_percent}\n"
            out_file.write(f"{text_data}")

main()