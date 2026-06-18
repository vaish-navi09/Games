import random
questions = {"capital of india?" : "delhi",
             "capital of UP?": "lucknow",
              "National game of india?": "hockey",
               "National bird of india?": "peacock",
               "How many states in India?":"29"}

ques_list = list(questions.keys())
random.shuffle(ques_list)
score = 0
for ques in ques_list:
    print(ques)
    ans = input("enter the ans").lower()
    if ans == questions[ques]:
        print("correct")
        score += 1
    else:
        print("wrong")
    
print(" Your Total score",score)
