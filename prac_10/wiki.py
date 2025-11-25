import wikipedia

def main():
    user_input = input("Enter page title: ")
    while user_input:
        print(wikipedia.page(user_input, auto_suggest=False))
        user_input = input("Enter page title: ")


main()
