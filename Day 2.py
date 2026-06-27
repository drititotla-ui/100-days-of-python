print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10 12 15 or custom?\n"))
people = int(input("How many people to split the bill? \n"))
total=(bill*tip/100+bill)
total_per_person =(bill*tip/100+bill)/people
print("your total bill is : "+str(total))
print(f"each person should pay ${total_per_person}")