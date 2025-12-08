n = int(input("Enter the number : "))
num = n
while(num != 0): # number print from the reverse
    res = num%10
    print(res,end=' ')
    num //= 10