#list can be initiated with arr = list() or with a few elements such as arr = [1,2,3]
#result of print arr[0] + arr[1] + arr[2] is 6
#multiple types of data can be added in a single list.
#list can be created of any object: strings, integers, or even lists themselves.


inputnum = int(input("Please enter the number of times you want to take the input : "))
arr = []

for num in range(0, inputnum):
    output = input("enter your Command: ")
    outputstr = output.split()

#    print("This is your command : " + outputstr[0])
#    print("This is your number : " + str(outputstr[1]))
#    print("This is your second number : " + str(outputstr[2]))
    if(str(outputstr[0]) == "append"):
        arr.append(int(outputstr[1]))
    if(str(outputstr[0]) == "insert"):
        arr.insert(int(outputstr[2]), int(outputstr[1]))
#        print(str(outputstr[0]))
#        print(str(outputstr[1]))
#        print(str(outputstr[2]))
    if(str(outputstr[0]) == "print"):
        print(arr)
    if(str(outputstr[0]) == "remove"):
        arr.remove(int(outputstr[1]))
    if(str(outputstr[0]) == "sort"):
        arr.sort()
    if(str(outputstr[0]) == "pop"):
        arr.pop()
    if(str(outputstr[0]) == "reverse"):
        arr.reverse()


#print(arr)