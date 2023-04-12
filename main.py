greeting = "Change Return Program"
print("How much money would you like to change? ")
initial_money = float(input("> "))
print(f"What type of change do you want? (pennies/nickels/dimes/quarters)")
denomination = input("> ").lower()
pennies = initial_money * 100
nickels = initial_money * 0.05
dimes = initial_money * 10
quarters = initial_money * 4

if denomination == "pennies":
    print(f"{pennies} pennies is your change from ${initial_money}")
elif denomination == "nickels":
    print(f"{nickels} nickels is your change from ${initial_money}")
elif denomination == "dimes":
    print(f"{dimes} dimes is your change from ${initial_money}")
elif denomination == "quarters":
    print(f"{quarters} quarters is your change from ${initial_money}")
