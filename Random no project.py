import random
max_range = input("Enter the range value ")
if max_range.isdigit():
    max_range = int(max_range)
    if max_range <=0:
        print("Enter the value greater than 0")
        quit()
else:
    print("Please enter a valid input")
    quit()
random_number = random.randint(0,max_range)
guess = 0
while True:
    guess+=1
    guess_value = input("Enter your response")
    if guess_value.isdigit():
        guess_value = int(guess_value)
    else:
        print("Please enter a valid input")
        continue
    if guess_value == random_number:
        print("Correct")
        break
    elif guess_value >=random_number:
        print("you are above the number")
    else:
        print("You are below the number")
print("You took",guess,"guess")
    