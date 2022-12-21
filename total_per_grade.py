# Python Programme for finding TOTAL MARKS, PERCENTAGE and GRADES

phy = int(input("Enter your PHYSICS marks: \n"))
che = int(input("Enter your CHEMISTRY marks: \n"))
bio = int(input("Enter your BIOLOGY marks: \n"))
math = int(input("Enter your Math marks: \n"))
eng = int(input("Enter your ENGLISH marks: \n"))

total = phy+che+bio+math+eng
per = total/500*100

print("-----Your RESULT is-----")
print("Total Marks: ",total)
print("Percentage: ",per)

if per >= 90 and per <= 100:
    print("Your Grade is A+")
elif per >=80 and per > 90:
    print("Your Grade is A")
elif per >=70 and per > 80:
    print("Your Grade is B")
elif per >=60 and per > 70:
    print("Your Grade is C")
elif per >=50 and per > 60:
    print("Your Grade is D")
else:
    print('''You are "Fail"''')
print("-----end of RESULT-----")
