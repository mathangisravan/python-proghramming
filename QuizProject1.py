
playing = input("Do you want to participate in quiz? ")
if playing.lower() != "yes":
    quit()

print("Lets start the Quiz now :)")
score = 0
answer = input("Q1. What is the fullform of CPU? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score+=1
else:
    print("Incorrect")
answer = input("Q2. What is the fullform of RAM? ")
if answer.lower() == "random access memory":
    print("Correct")
    score+=1
else:
    print("Incorrect")
answer = input("Q3. What is the fullform of ROM? ")
if answer.lower() == "read only memory":
    print("Correct")
    score+=1
else:
    print("Incorrect")
answer = input("Q4. What is the fullform of HTTP? ")
if answer.lower() == "hyper text transfer protocol":
    print("Correct")
    score+=1
else:
    print("Incorrect")
answer = input("Q5. What is the fullform of WWW? ")
if answer.lower() == "world wide web":
    print("Correct")
    score+=1
else:
    print("Incorrect")
answer = input("Q6. What is the fullform of MB? ")
if answer.lower() == "mega bite":
    print("Correct")
    score+=1
else:
    print("Incorrect")
answer = input("Q7. What is the fullform of POST? ")
if answer.lower() == "power on self test":
    print("Correct")
    score+=1
else:
    print("Incorrect")
answer = input("Q8. What is the fullform of IT? ")
if answer.lower() == "information technology":
    print("Correct")
    score+=1
else:
    print("Incorrect")
answer = input("Q9. What is the fullform of CSE? ")
if answer.lower() == "computer science and engineering":
    print("Correct")
    score+=1
else:
    print("Incorrect")


print("You have answered",score,"questions Correctly :) ")