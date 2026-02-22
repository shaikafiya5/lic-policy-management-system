import random
options=["stone ","paper","scissor"]
computer=random.choice(options)
user=input("enter your choise stone paper scissor")
print("computer chose",computer)
if computer==user:
    print("game tie")
elif user=="stone" and computer=="paper":
    print("you win the game stone kills paper")
elif user=="paper" and computer =="stone":
    print("you losse stone diamage paper")
elif user=="scissor"and computer=="paper":
    print("you win scissor cuts paper")
else:
    print("invalid input please inter valid input")


































