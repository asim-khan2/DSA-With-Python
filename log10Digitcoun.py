import math 

num = int(input("Enter the number : "))

if num == 0:
    coutn = 1
else :
    count = int(math.log10(abs(num))) + 1
print("Number of digit is : ", count)
