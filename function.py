# This is my own written solution
year = input("Please enter your year : ")
if(1900 <= int(year) <= 100000):
	if(int(year)%4==0):
		if(int(year)%400==0):
			print("This is a leap year.")
		elif(int(year)%100==0):
			print("This is not a leap year.")
		else:
			print("This is a leap year")
	else:
		print("This is a not a leap year")
else:
	print("Please input a valid year within the range")



#This is HackerRank's solution.
def is_leap(year):
	leap = False

	if year%400==0:
		return True
	elif year%100==0:
		return False
	elif year%4==0:
		return True

year = int(input())
print(is_leap(year))



#Notes on Functions in Python
#sample function
# def sample_function():				- A function with the name sample_function has been defined
#	print("Hello from a function")		- Some data is being returned from the function
#sample_function()						- This calls the function which makes the function to perform a certain actions
#
#Information can be passed into the function as arguments. Arguments are specified after the function name inside the parentheses. we can add as many arguments as we want and can seperate them with a comma.
#input1 = input("Please enter this as your first input : ")
#input2 = input("Please enter this as your second input : ")
#def sample_function(argument, argument2):		#If the number of arguments is not known, then a * should be added before the parameter name.
#    print(argument + " and " + argument2 + " is entered by the user")
#sample_function(input1, input2)
#
#
#
#
#
#
#
#
#
#
#	
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 