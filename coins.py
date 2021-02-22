print("Please enter the amount of money to convert:")
no_of_dollars= int(input("# of dollars: "))
no_of_cents= int(input("# of cents: "))
remaining_cents= no_of_dollars*100 + no_of_cents
no_of_quarters= remaining_cents//25
remaining_cents=remaining_cents%25
no_of_dimes= remaining_cents//10
remaining_cents=remaining_cents%10
no_of_nickels= remaining_cents//5
remaining_cents=remaining_cents%5
no_of_pennies= remaining_cents
print("The coins are",no_of_quarters,"quarters,",no_of_dimes,"dimes,",no_of_nickels,"nickels and",no_of_pennies,"pennies")