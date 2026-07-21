#Student Management System
student=dict()
while True:
    print("===========Student Management System===========")
    print("1.\t TO ADD NEW STUDENT")
    print("2.\t TO VIEW STUDENTS")
    print("3.\t TO SEARCH STUDENT")
    print("4.\t TO UPDATE STUDENT")
    print("5.\t TO DELETE STUDENT")
    print("6.\t TO SAVE RECORDS")
    print("7.\t TO EXIT")
    ch = int(input(">"))
    if ch == 1:
        print("===========Enter Student Information============")
        id = int(input("Enter Student ID: \n"))
        name = input("Enter Student Name: \n")
        age = int(input("Enter Student Age: \n"))
        course = input("Enter Student Course: \n")
        marks = eval(input("Enter Student Marks: \n"))
        student[id] = {"name": name, "age": age, "course": course, "marks": marks}
    elif ch == 2:
        print("===========ALL Student Information============")
        for key in student.keys():
            print(f'id:\t{key}')
            print(f'Name:\t{student[key]["name"]}')
            print(f'Age:\t{student[key]["age"]}')
            print(f'Course:\t{student[key]["course"]}')
            print(f'Marks:\t{student[key]["marks"]}')
            print("---------------------------------------------")
        print("==============================================")
    elif ch == 3:
        searchId = int(input("Enter Student ID: \n"))
        flag=0
        for key in student.keys():
            if key == searchId:
                flag=1
                print(f'id:\t{key}')
                print(f'Name:\t{student[key]["name"]}')
                print(f'Age:\t{student[key]["age"]}')
                print(f'Course:\t{student[key]["course"]}')
                print(f'Marks:\t{student[key]["marks"]}')
                print("---------------------------------------------")
                print("==============================================")
            if flag==1:
                break
        if flag==0:
            print('Student not found.')
    elif ch == 7:
        break
    else:
        print("==========Enter valid input==========")








