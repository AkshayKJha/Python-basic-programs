price_first= float(input("Enter price of the first item: "))
price_second= float(input("Enter price of the second item: "))
club_member= input("Does customer have a club card? (Y/N): ")
tax_rate= float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))

base_price=price_first+price_second


if(price_first<price_second):
    discount=price_first/2
else:
    discount=price_second/2

discounted_price=base_price-discount

if (club_member=='Y' or club_member=='y'):
    discounted_price=discounted_price*(0.9)
tax=discounted_price*(tax_rate/100)
total_price=round(discounted_price+tax,2)

print ("Base price = {:2.2f}".format(base_price))
print ("Price after discounts = {:2.2f}".format(discounted_price))
print ("Total price = {:2.2f}".format(total_price))
