# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name01 = input("What is your name? \n")
name02 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name01.lower()
name2 = name02.lower()
count_l = name1.count("l") + name2.count("l")
count_o = name1.count("o") + name2.count("o")
count_v = name1.count("v") + name2.count("v")
count_e = name1.count("e") + name2.count("e")
count_t = name1.count("t") + name2.count("t")
count_r = name1.count("r") + name2.count("r")
count_u = name1.count("u") + name2.count("u")
count_e2 = name1.count("e") + name2.count("e")
add_love = count_l + count_o + count_v + count_e
add_true = count_t + count_r + count_u + count_e2
score = str(add_true) + str(add_love)
score_int = int(score)
if score_int < 10 or score_int > 90 :
    print(f"Your score is {score_int}, you go together like coke and mentos.")
elif score_int >= 40 and score_int <= 50 :
    print(f"Your score is {score_int}, you are alright together.")
else : 
    print(f"Your score is {score_int}.")     