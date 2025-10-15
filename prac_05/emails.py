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
    email = input("Enter e-mail address: ")
    email_to_name[email] = extract_name(email)
    while email != '':
        email = input("Enter e-mail address: ")
        email_to_name[email] = extract_name(email)
    print(email_to_name)

def extract_name(email):
    remove_mail = email.split("@")
    names = remove_mail[0].split(".")
    whole_name = (remove_mail[0] + " " + remove_mail[1])
    return whole_name

main()