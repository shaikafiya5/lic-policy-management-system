import time
quiz=[{"question":"python is language or snake",
      "option":["A)LANGUAGE ", "B)GAME",  "C) SNAKE ONLY", "D)BROWSER "],"answer":"A"},
{ "question": "2 +2 =?",
  "option":["A) 3", " B)4", " C)0", " D)1"],"answer":"B"},
 {"question":"capital of india",
  "option":["A) delhi","B) mumbai","C) chennai","D) kolkata"],"answer":"A"}]
score=0
time_limit=10
print("====== WELCOME TO QUIZ=======")
for q in quiz:
    print(q["question"])
    for opt in q["option"]:
        print(opt)
    start=time.time()
    user=input("your answer (A/B/C/D) ").upper()
    end=time.time()
    if end-start>time_limit:
        print("Time up")
        continue
    if user==q["answer"]:
        print("correct")
        score+=1
    else:
        print("wrong ! correct answer is",q["answer"])
print("======Result======")
print("your score",score,"/",len(quiz))









