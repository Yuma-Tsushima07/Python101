print('Challenge 11: WAF to print factorial of a number.')

num = int(input("Enter a number:"))
Fact = 1
for i in range(1, num + 1):
    Fact = Fact * i
print("The Factorial of",num,"is",Fact)