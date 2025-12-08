num = int(input("Enter the number : "))
count = 0
n = num
while(n != 0): # count the nuber 
    count += 1
    n //= 10
print("count is : ", count)