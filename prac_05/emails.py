"""
CP1404 Practical
Email name extraction
Date: 15.10.2025
Author: Nicola Culik
Estimate: 50 min
Actual:  min
"""

def main():
    email_to_name = {}
    print(email_to_name)
    email = input("Email: ")
    # whole_name = extract_name(email)
    # email_to_name[email] = validate_name(whole_name)
    while email != '':
        whole_name = extract_name(email)
        email_to_name[email] = validate_name(whole_name)
        email = input("Email: ")
    print(email_to_name)

def extract_name(email):
    remove_mail = email.split("@")
    names = remove_mail[0].split(".")
    whole_name = " ".join(names).title().strip()
    return whole_name

def validate_name(whole_name):
    choice = input(f"Is your name {whole_name}? (Y/n)").upper()
    if choice == "Y" or choice == "":
        return whole_name
    else:
        whole_name = input("Name: ").title()
        return whole_name

main()