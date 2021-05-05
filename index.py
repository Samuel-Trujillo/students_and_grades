students = []
student_count=1000


student_count= int(input("How many students do you have?  "))
for i in range(student_count):
    addkeys= ('Name', 'Grade', 'Course')
    adddict= dict.fromkeys(addkeys)
    students.append(adddict)
    name= input("Students name:  ")
    students[i]['Name']= name
    grade= input("Students grade:  ")
    students[i]['Grade']= grade
    course= int(input("Select a course 1- Math, 2- Science, 3- History:  "))
    if course == 1:
        course = 'Math'
    if course == 2:
        course = 'Science'
    else:
        course = 'History'
    students[i]['Course']= course
    student_count -= 1
    


print(students)

