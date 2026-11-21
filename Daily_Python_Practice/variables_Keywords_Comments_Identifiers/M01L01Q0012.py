
# 2. Salary Planner

# Store target monthly income
target_monthly_income = 10000000

# Calculate yearly income (monthly income * 12)
yearly_income = target_monthly_income * 12

# Calculate 30% tax on yearly income
tax_amount = yearly_income * 30 / 100

# Calculate yearly take-home salary after tax
take_home_pay = yearly_income - tax_amount

# Calculate monthly take-home salary
monthly_take_home_pay = take_home_pay / 12

# Display results
print("Target Monthly Income:", target_monthly_income)
print("Yearly Income:", yearly_income)
print("30% Tax Amount:", tax_amount)
print("Yearly Take-Home Pay:", take_home_pay)
print("Monthly Take-Home Pay:", monthly_take_home_pay)


"""Target Monthly Income: 10000000
Yearly Income: 120000000
30% Tax Amount: 36000000.0
Yearly Take-Home Pay: 84000000.0
Monthly Take-Home Pay: 7000000.0"""