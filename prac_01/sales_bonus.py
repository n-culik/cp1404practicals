"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
TOP_BONUS = 0.15
LOW_BONUS = 0.10

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        user_bonus = sales * LOW_BONUS
        print(f"Bonus: ${user_bonus:.0f}")
    else:
        user_bonus = sales * TOP_BONUS
        print(f"Bonus: ${user_bonus:.0f}")
    sales = float(input("Enter sales: $"))