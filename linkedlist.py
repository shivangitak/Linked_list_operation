l1=[]
l1.append('america')
l1.append('russia')
l1.append('dubai')
print("the exixtisting list is :",l1)
choice=0
while choice<5:
    print('1 for add element')
    print('2 for remove element')
    print('3 for replace element')
    print('4 for search element')
    print('5 Exit')
    choice= int(input("Enter choice"))
    if choice==1:
        element=(input("enter appending element"))
        pos=int(input("which position:"))
        l1.insert(pos,element)
    elif choice==2:
        try:
            element = (input("enter deleting element"))
            l1.remove(element)
        except ValueError:
            print("element not found")
    elif choice==3:
        element=(input("enter replace new element"))
        pos=int(input("in which positon :"))
        l1.pop(pos)
        l1.insert(pos,element)
    elif choice==4:
        try:
            element=input("enter finding element:")
            pos=l1.index(element)
            print("element at index",pos)
        except ValueError:
            print("element not found")
    else:
        break
    print(l1)
