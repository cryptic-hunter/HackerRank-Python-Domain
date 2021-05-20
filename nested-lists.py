from operator import itemgetter

numstu = int(input("Please enter the number of students in the class : "))

marksheet = []

for i in range(0,numstu):
    name = input("Please enter name of the student : ")
    marks = float(input("Please enter scores of the student : "))
    marksheet.append([name,marks])

sortedlist = sorted(marksheet, key=itemgetter(1))

second_lowest = sortedlist[1]

lowest_list = []
for stu in marksheet:
    print(second_lowest)


#This is an incomplete solution.