

def findMax(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        print(str(num1) + ' is the greatest number among the three')
    elif (num2 > num1 and num2 > num3):
        print(str(num2) + ' is the greatest number among the three')
    else:
        print(str(num3) + ' is the greatest number among the three')

print('Enter the first number')
num1 = input()
print('Enter the second number')
num2 = input()
print('Enter the third number')
num3 = input()

findMax(num1, num2, num3)