import random 
i = random.randint(1,11)
user_name = str(input("Enter your name : "))
print("Welcome to the game " +user_name)
k = 1
while k <= 5:
    a = int(input("Enter a number N : "))
    if a == i: 
        print(f"Correct answer in {k} tries")
        break
    elif a < i: 
        print("Take a higher guess")
    else: 
        print("Take a lower guess")
    k = k + 1

print(f"Correct guess is : {i}")