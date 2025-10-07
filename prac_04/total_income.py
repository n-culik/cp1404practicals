"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
Date: 07.10.2025
"""


def main():
    """Display income report for incomes over a given number of number_of_months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for i in range(0, len(incomes)):
        total += incomes[i]
        print(f"Month {i+1:2} - Income: ${incomes[i]:10.2f} Total: ${total:10.2f}")

main()
