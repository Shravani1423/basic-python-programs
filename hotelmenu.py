menu ={
'pizza':60,
'burger':50,
'pasta':70,
'momoze':40,
'coffee':70,
}


print("welcome our PYTHON restaurant !" )

print(" pizza: 60\n burger:50\n pasta:70\n momoze:40\n coffee:70")

total_order= 0

itam1 = input("Enter the name of order you wanted = ")
if itam1 in menu :
    total_order += menu[itam1]
    print(f"your itame {itam1} has been added to your order. ")

else:
    print(f"sorry !{itam1} is not avalibale") 
anoter_order= input("Do you want to another item? (yes/no) ")
if anoter_order =="yes":
    itam2= input("Enter your second order = ")
    if itam2 in menu:
        total_order += menu[itam2]
        print(f"itam {itam2} is added in your order")
    else:
        print(f"sorry !{itam2} is not avalibale") 

print(f"the total amount of itams is,to pay {total_order}")        
