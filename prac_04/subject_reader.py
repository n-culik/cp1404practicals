"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_infos = load_data(FILENAME)
    print_subject_info(subject_infos)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_infos = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        subject_info = line.split(',')  # Separate the data into its subject_info
        print(subject_info)  # See what the subject_info look like (notice the integer is a string)
        subject_info[2] = int(subject_info[2])  # Make the number an integer (ignore PyCharm's warning)
        print(subject_info)  # See if that worked
        print("----------")
        subject_infos.append(subject_info)
    input_file.close()
    return subject_infos

def print_subject_info(subject_infos):
    """Print structured subject info."""
    teacher_lenght = max(len(subject_info[1]) for subject_info in subject_infos)
    number_of_student_lenght = max(len(str(subject_info[2])) for subject_info in subject_infos)

    for subject in subject_infos:
        print(f"{subject[0]} is taught by {subject[1]:{teacher_lenght}} and has {subject[2]:{number_of_student_lenght}} students")
main()