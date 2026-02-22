policies={}
def add_policy():
    pid=int(input("Enter the policy id"))
    name=input("Enter the customer name")
    premium=int(input("Enter the premium amount"))

    policies[name]={"pid":pid,"premium":premium}
    print("=====policies added successfully=====")
def view_policy():
    if not policies:
        print("no policy found")
        return

    for name,info in policies.items():
            print(f"name: {'name'}")
            print(f"pid: {info['pid']}")
            print(f"premium :{info['premium']}")

def search_policy():
    name=input("Enter the name")
    if name in policies:
        print(policies[name])
    else:
        print("policy not fount")
def update_policy():
    name=input("Enter the name")
    if name in policies:

        new_pid=input("Enter the new pid(Enter to skip):")
        if new_pid!="":
            policies[name]["pid"]=int(new_pid)
        new_name=input("Enter the new name (Enter to skip)")
        if new_name!="":
            policies[new_name]=policies.pop(name)
            name=new_name
        new_premium=input("Enter the new premium (Enter to skip:)")
        if new_premium!="":
            policies[name]["premium"]=int(new_premium)
        print("updated successfully")
    else:
        print("Not found policy")
def delete_policy():
    global policies
    name=input("Enter the name")
    if name in policies:
        del policies
        print("Deleted successfully")    
    else:
        print("not fount policy")

while True:
    print(1, "add policy")
    print(2 ,"view policy")

    print(3," search policy")

    print(4," update policy")

    print(5," delete policy")


    choice=int(input("Enter your choice"))
    if choice==1:
        add_policy()
    elif choice==2:
        view_policy()
    elif choice==3:
        search_policy()
    elif choice==4:
        update_policy()
    elif choice==5:
        delete_policy()
        break
    else:
        print("invalid policy")


