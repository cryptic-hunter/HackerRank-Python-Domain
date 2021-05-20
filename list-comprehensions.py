#given 3 integers x,y and z. representing the dimensions of a cuboid along with integer n. 
#print a list of all possible coordinates, given by (i,j,k) on a 3d graph where sum of i+j+k is not equal to n. 

x = int(input("Please enter the value of x : "))
y = int(input("Please enter the value of y : "))
z = int(input("Please enter the value of z : "))
n = int(input("Please enter the value of n : "))

res = [[i,j,k] for i in range(0, x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n]
print(res)
