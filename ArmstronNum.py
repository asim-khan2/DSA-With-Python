num = int(input("Enter the number : "))
# l = len(str(num)) #it will give the length of the number 
l = 0
n = num
palin = 0
while(n > 0): # here we calculate the length  
    l += 1
    n //= 10
temp = num
while(temp > 0):
    rem = temp % 10
    palin += rem ** l
    temp //= 10

if num == palin:
    print(f"{num} & {palin} \nNumber is palindrom")
else:
        print(f"{num} & {palin} \nNumber isn't palindrom")