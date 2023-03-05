print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? "))
percentage = int(input("What percentage would you like to tip your waiter? 10, 15, 18, or 20? "))
tip_percent = (percentage / 100) 
bill_tip = bill + tip_percent
total_bill = bill + bill_tip
people = int(input("How many people to split the bill? "))
split = total_bill / people
split_round = round(split, 2)
print(f"Each person should pay: ${split_round}")
