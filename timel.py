import time
## morning 4 to 11:59
## afternoon 12 to 16:59
## evening 17 to 20:59
##good night 21 to 3:59
name=input("enter your name")
hour=int(input(time.strftime(':%h')))
if 4<=hour <=11:
    print("goog morning",name)
elif 12<=hour <=16:
    print("good afternoon",name)
elif 17<=hour<=20:
    print("good evening",name)
elif 21<=hour <=3:
    print("good night",name)










