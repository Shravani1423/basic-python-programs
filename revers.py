n = int(input ("enter the numbers : "))
r = 0
while(n > 0):
    rem =n%10
    r =r*10+rem
    n =int(n/10)
print("revers no is :",r)
