print("Prpgramme for finding ODD and EVEN numbers in list")

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even = []
odd = []

print('---------------------------------------------------')
print('Given List :',list1)
print('Total Numbers in list before finding EVEN and ODD numbers : ',len(list1))
print('---------------------------------------------------')

for i in list1:
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)

print('---------------------------------------------------')
print('List of EVEN numbers: ',even)
print('Total EVEN Numbers in given list: ',len(even))
print('---------------------------------------------------')
print('List of ODD numbers: ',odd)
print('Total ODD Numbers in given list: ',len(odd))
print('---------------------------------------------------')
