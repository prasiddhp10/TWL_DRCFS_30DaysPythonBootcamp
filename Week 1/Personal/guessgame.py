import random
i = random.randint(0,10)
for k in range(5):
    a = int(input("Enter a number below 10: "))
    if i == a: 
        print(f"Correct answer in {k+1} tries")
        break
    elif i < a: 
        print("Guess a lower number")
    else: 
        print("Guess a higher number")

print(i)