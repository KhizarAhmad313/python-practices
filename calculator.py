print('***Simple Calculator in Python by KHIZAR AHMAD***')
print('''Use "+ - / * all" sign for calculation''')
print('------------------------------------------------')

num1 = int(input('Enter your first number \n'))
num2 = int(input('Enter your second number \n'))

print('------------------------------------------------')
print('Your Have Entered These Two Numbers', num1, num2 )
print('------------------------------------------------')

add = num1 + num2
sub = num1 - num2
div = num1 / num2
mul = num1 * num2

op = input('Type which operation you want to perform \n')

if op == "+":
    print('Addition of your Numbers is ', add)
elif op == "-":
    print('Subtraction of your Numbers is ', sub)
elif op == "/":
    print('Division of your Numbers is ', div)
elif op == "*":
    print('Multiplication of your Numbers is ', mul)
elif op == "all":
    print('Addition of your Numbers is ', add)
    print('Subtraction of your Numbers is ', sub)
    print('Division of your Numbers is ', div)
    print('Multiplication of your Numbers is ', mul)
else:
    print('ERROR!!! Please enter correct sign.')
