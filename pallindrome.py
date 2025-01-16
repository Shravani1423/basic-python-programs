list = []
list.append(input("Enter item : "))
list.append(input("Enter item : "))
list.append(input("Enter item : "))
print(list)
copy_list =list.copy()
copy_list.reverse()
if (copy_list ==list):
    print("pallindrome")
else:
    print("not pallindrome")