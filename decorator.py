def decorator(f):
    def doWork(*val):
        print("good morning")
        f(*val)
        print("thank you for using this function")
    return doWork

@decorator
def info(n,o):
    name=n
    occupation=o
    print(f"{name} is working as a {occupation}")
@decorator
def add(a,b):
    print(a+b)

info("afiya","developer")
add(2,3)






































