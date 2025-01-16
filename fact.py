num = int(input("Entrr the number to find factorial : "))
fact =1
if num < 0:
    print("do't find factorial becouse number is negative ")
elif num ==0:
    print("0 is factorial is 1" )
else:
    for i in range(1, num+1):
        fact *= i
    print("The factorial of",num,"is",fact)

