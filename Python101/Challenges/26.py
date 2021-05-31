print("Challenge 26: Write a Python program to find the number of zeros at the end of a factorial of a given positive number.")

import math

num = int(input("Enter a number: "))

factorial = math.factorial(num)


def end_zeros():
    new_num = str(factorial)
    count = len(new_num) - len(new_num.rstrip("0"))
    return count

print(end_zeros())