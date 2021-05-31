print('Challenge 7: WAF to return sum of 3 number.')

num1 = float(input("Input the num1: "))
num2 = float(input("Input the num2: "))
num3 = float(input("Input the num3: "))


def function(num1, num2, num3):
   if num1 == num2 == num3:
     return 3 * (num1 + num2 + num3)
   else:
      return num1 + num2 + num3


print(function(num1, num2, num3))