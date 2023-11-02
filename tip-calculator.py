print("welcome to the tip calculator.")

bill = input("What is the total bill? $")
print('')
tip_percentagae = input("What percentage tip would you like to give 10, 12, or 15? ")
print('')
people = input("How many people to split the bill? ")
print('')
tip = (float(bill)) * (float(tip_percentagae) /100)

tip2 = (float(tip )/float(people))

over_all_bill = float(bill) /float(people)

Total_bill = float(over_all_bill) + float(tip2)

Display = round(Total_bill, 2)

print(f"Each person should pay: $ {Display} Birr")
