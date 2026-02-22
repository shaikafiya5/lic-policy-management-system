students={}
def add_student():
    sid=int(input("Enter the student id"))
    name=input("Enter the student name")
    age=int(input("Enter the student age"))
    grade=input("Enter Grade")
    students[sid]={"name":name,"age":age,"grade":grade}
    print("Student added successfully")

def view_students():
    if not students:
        print("No record found")
        return
    for sid,info in students.items():
        print(f"id :{sid}")
        print(f"name :{info['name']}")
        print(f"age :{info['age']}")
        print(f"grade: {info['grade']}")
        print("--------------------")
def search_student():
    sid=int(input("Enter the student id"))
    if sid in students:
        print(students[sid])
    else:
        print("not found")
def update_student():
    sid=int(input("Enter the id"))
    if sid in students:
        students[sid]['name']=input("Enter the new name")
        students[sid]['age']=int(input("Enter the new age"))
        students[sid]['grade']=input("Enter the new grade")
        print("Updated successfully")
    else:
        print("not fount ")
def delete_student():
    sid=int(input("Enter the student id"))
    if sid in students:
        del students[sid]
        print("Deleted successfully")
    else:
        print("not found")

while True:
    print("1,add Student")
    print("2,view Student")
    print("3,search student")
    print("4,update student")
    print("5,delete student")

    choice=int(input("Enter the choice"))
    if choice==1:
        add_student()
    elif choice==2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice==4:
        update_student()
    elif choice==5:
        delete_student()
        break
    else:
        print("invalid input")




