import random
i = random.randint(0,10000)
for i in range(10):
    a = int(input("Enter a number below 10000: "))
    if i == a: 
        print("Correct guess")
        end()
    elif i < a: 
        print("Guess a lower number")
    else: 
        print("Guess a higher number")

print(i)