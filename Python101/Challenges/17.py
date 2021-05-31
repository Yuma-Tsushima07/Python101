print('Challenge 17: WAF to calculate GCD of 2 positive numbers')

num1 = float(input(" Please Enter the First Value  Num1 : "))
num2 = float(input(" Please Enter the Second Value Num2 : "))

a = num1
b = num2

while(num2 != 0):
    temp = num2
    num2 = num1 % num2
    num1 = temp

gcd = num1   
print("\n HCF of {0} and {1} = {2}".format(a, b, gcd))