print('enter the two numbers')
num1 = float(input())
num2 = float(input())
if num1+0.001==num2:
    print("close")
elif num2+0.001==num1:
    print("close")
else:
    print("Not Close")

