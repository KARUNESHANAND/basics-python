#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to bill calculator")
total_bill = float(input("What was the total bill?"))
tip_bill = int(input("How much tip do u want to tip the waiter? 10 or 12 or 15?"))
peeps_split = int(input("How many people to split the bill?"))
final_amount_paid_by_each = (total_bill / peeps_split) * (1+(tip_bill/100))
round_final = "{:.2f}".format(final_amount_paid_by_each)
print(f"Each person should pay {round_final}")

