print("Python Programme for printing pattern")
print("------------------------------")

num = int(input("Enter Rows: \n"))

print("-----OUTPUT-----")

for i in range(1, num+1):
    for j in range(1, i+1):
        print("@",end=" ")
    print()
 
print("---END of OUTPUT---")
