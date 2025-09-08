grades={}
while True:
    print("1. Add student\n2. Update Grade\n3. View students\n4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter student name: ")
        grade=input("Enter student grade: ")
        grades[name]=grade
    if choice==2:
        name=input("Enter student name: ")
        if name in grades:
            grade=input("Enter new grade: ")
            grades[name]=grade
        else:
            print("Student not found")
    if choice==3:
        print("Student List:",grades)
    if choice==4:
        break
