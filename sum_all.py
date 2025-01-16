num =int(input("Enter the number "))
sum =0
while(num > 0):
    rem =num%10
    sum =sum+ rem
    num =int(num/10)
print("sum of numbers is : ",sum)