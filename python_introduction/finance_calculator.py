monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
interest_rate = 5
annual_savings = (monthly_savings * 12 + (monthly_savings * 12 * interest_rate / 100))
print("Your monthly savings are $", monthly_savings, "and your projected annual savings are $", annual_savings)