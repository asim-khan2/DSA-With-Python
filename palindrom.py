num = int(input("Enter the number : "))

temp = num # store the num for the compare wheather equal or not
reversed = 0

while(temp > 0):
    rem = temp % 10
    reversed = reversed * 10 + rem # calculate the reverse
    temp //= 10

if reversed == num: # check the wheather no. is palindrom
    print(f"{num} = {reversed} \nnumber is palindrom")

else:
    print(f"{num} X {reversed} \nnumber is not palindrom")