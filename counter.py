print("Please enter the number of coins:")
no_of_quarters= int(input("# of quarters: "))
no_of_dimes= int(input("# of dimes: "))
no_of_nickels= int(input("# of nickels: "))
no_of_pennies= int(input("# of pennies: "))
total_in_cents= (no_of_quarters*25) + (no_of_dimes*10) + (no_of_nickels*5) + no_of_pennies
dollars=total_in_cents // 100
cents=total_in_cents % 100
print("The total is",dollars,"dollars and",cents,"cents")