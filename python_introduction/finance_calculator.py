monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your monthly expenses: ")

monthly_savings = float(monthly_income) - float(monthly_expenses)

Projected_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)

print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Projected savings in one year with interest: ${Projected_savings:.2f}")
