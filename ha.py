import math


def loan_schedule(amount, annual_rate,years, extra_payment=0, deposit=0):
    principal = amount - (deposit or 0)
    monthly_rate = annual_rate / 12 /100
    months = years *12
    
    monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    balance = principal
    schedule = []

    for m in range(1, months + 1):
        interest = balance * monthly_rate
        principal_payment = monthly_payment - interest

        
        if m == 1 and extra_payment > 0:
            principal_payment += extra_payment

        balance -= principal_payment
        if balance < 0:
            balance = 0

        schedule.append({
            "Month": m,
            "Monthly Payment": round(monthly_payment),
            "Interest": round(interest),
            "Principal Payment": round(principal_payment),
            "Remaining Balance": round(balance)
        })

        if balance <= 0:
            break

    return schedule



amount = 100_000_000
annual_rate = 13
extra_payment = 10_000_000

for years in [1, 2, 3, 4, 5]:
    print(f"\nLoan term: {years} year(s)")
    schedule = loan_schedule(amount, annual_rate, years, extra_payment)
    for row in schedule[:12]:  
        print(row)
