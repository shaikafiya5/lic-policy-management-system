questions=[
    ["which language is used to write python program?","python","java","c","c++",1],
    ["which data type store string in python" ,"int","float","string","none",3],
    ["which key word is used to handle the exception in python","catch","try","error","handle",2]
    ]
money=0
PrizeMoney= 100,200,300,
for i in range(0,len(questions)):
    question=questions[i]
    print(question[0])
    print(f" a.{question[1]}    b.{question[2]}")
    print(f" c.{question[3]}      d.{question[4]}")
    reply=(int(input("enter your answer from 1-4")))
    if reply==question[-1]:
        print("your answer is correct ")
        if(i==3):
            print(f"total {PrizeMoney[i]} you won ")
        else:
            print(PrizeMoney[i])
    else:
        print("your answer is wrong")
        break



































