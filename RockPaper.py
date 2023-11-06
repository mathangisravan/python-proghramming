import random
outcomes = ["rock","paper","scissors"]
comp_score =0
human_score = 0
while True:
    user_input = input("Please selcet Rock/Paper/Scissors/ or Q to quit ?\n").lower()

    if user_input == "q":
        quit()
    if user_input not in outcomes:
        print("Please provide a valid input ")
        continue
    random_no = random.randint(0,2)
    computer_ans = outcomes[random_no]
    print("Computer picked ",computer_ans)
    if user_input == "rock" and computer_ans == "scissors":
        print("User win")
        human_score+=1
        continue
    if user_input =="scissors" and computer_ans == "paper":
        print("User win")
        human_score+=1
        continue
    if user_input == "paper" and comp_score == "rock":
        print("User won")
        human_score+=1
    else:
        print("Computer Won")
        comp_score+=1
        continue
print("Bye")
print("User won ",human_score,"times")
print("computer won",comp_score,"times")


