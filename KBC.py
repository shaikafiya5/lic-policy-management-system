question=[["1.what is your name"],["2.what is your age"],["3.your home town"]]
options=([["a) afiya "],["b).aliya"],["c)aquib"],["d)shaik"]],["a).[12]","b).[21]","c).[30]","d).[40]"],
         [["a).hdp"],["b).atp"],["c).hyd"],["d).blg"]])
answers=["a","b","a"]
prizeMoney=["100","200","300"]
print("welcome to game")
for i in range(len(question)):
    print(question[i])
    for opt in options[i]:
        print(opt)
    userAnswer=input("enter your answer")
    if userAnswer==answers[i]:
       print("geate your answer is correct")
       print("you won the ",prizeMoney[i])
    else:
       print("your answer is wrong ")

print("your game ends hear")











