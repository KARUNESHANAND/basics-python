# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S" :
    if add_pepperoni == "Y" :
        if extra_cheese == "Y" :
            print("Your final bill is: $18.")
        elif extra_cheese == "N":
            print("Your final bill is: $17.")
    elif add_pepperoni == "N" :
        if extra_cheese == "Y" :
            print("Your final bill is: $16.")
        elif extra_cheese == "N":
            print("Your final bill is: $15.")
elif size == "M" :
    if add_pepperoni == "Y" :
        if extra_cheese == "Y" :
            print("Your final bill is: $24.")
        elif extra_cheese == "N":
            print("Your final bill is: $23.")
    elif add_pepperoni == "N" :
        if extra_cheese == "Y" :
            print("Your final bill is: $21.")
        elif extra_cheese == "N":
            print("Your final bill is: $20.")
elif size == "L" :
    if add_pepperoni == "Y" :
        if extra_cheese == "Y" :
            print("Your final bill is: $29.")
        elif extra_cheese == "N":
            print("Your final bill is: $28.")
    elif add_pepperoni == "N" :
        if extra_cheese == "Y" :
            print("Your final bill is: $26.")
        elif extra_cheese == "N":
            print("Your final bill is: $25.")
else :
    print("Invalid inputs")
