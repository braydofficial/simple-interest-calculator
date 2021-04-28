# A simple tool to calculate the estimated yearly interest
print("How many years do you plan saving money?")
years = int(input("Enter years: "))

print("How much money do you currently have?")
current_holdings = float(input("Enter your current account holdings: "))

print("What do you plan to invest every month?")
invest = float(input("Enter amount: "))

print("What do your estimate your yearly interest would be?")
interest = float(input("Enter interest in decimals (10% = 0.1): "))

print(' ')

invest = invest * 12
final_amount = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = current_holdings
    
    final_amount = (final_amount + invest) * (1 + interest)
    # Round the final amount, so it doesn't have dozens of useless decimals
    final_amount = round(final_amount)

print("You would have the following amount in your account after {} years: ".format(years) + str(final_amount))