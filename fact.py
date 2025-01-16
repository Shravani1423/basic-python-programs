num=int(input("enter the number:"))
fact=1
if num<0:
    print("number is negitive")
elif num==0:
    print("0 is factorial is 1")
else:
    for i in range(1,num+1):
        fact*=i
    print("factorial :",fact)
        