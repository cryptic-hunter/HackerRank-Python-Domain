from collections import defaultdict

num_stu = int(input("Please enter the number of students : "))

marks = {}

for i in range(1,num_stu+1):
    name, marks1, marks2, marks3 = input("Enter the name and marks of the student: ").split()
    globals()[f"d{i}"] = print(f"This was from {i} iteration")
    print("Name of the Student is : " + name)
    print("Marks in 1st Subject are : " + str(marks1))
    print("Marks in 2nd Subject are : " + str(marks2))
    print("Marks in 3rd Subject are : " + str(marks3))

