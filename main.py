# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)
#print(num_items)
bill = random.randint(0 , num_items - 1)
pay = names[bill]
print(f"{pay}  will pay the bill today !!")
