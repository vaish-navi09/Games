import random
choices= ["rock","paper","scissors"]
user_score = 0
computer_score = 0
for i in range (5):
    user = input("enter the choice")
    computer = random.choice(choices)
    print("user ", user)
    print("computer", computer)
  
    if user == computer :
        print("draw")
    elif (user== "rock" and computer == "scissors") or\
          (user == "scissors" and computer == "paper") or\
           (user== "paper"and computer=="rock"):
        print("user win!")
        user_score += 1
    else:
        print("computer win!")
        computer_score += 1
    print(user_score)
    print(computer_score)
if user_score >computer_score:
    print("game winner user")
elif computer_score > user_score:
    print("game winner computer")
else:
    print("match draw")
    
    
    
    