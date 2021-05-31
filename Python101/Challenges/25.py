print("Challenge 25: Write a Python program to find the median among three given numbers.")

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number : "))

sum = num1 + num2 + num3
x = max(num1 , num2,num3)
y = min(num1 , num2 , num3)
median = sum - x- y
print("The median: ",median)