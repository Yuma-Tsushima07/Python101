import random
print("Challenge 21: Write a Python program to create the combinations of 3 digit combo")

numbers = range(10)
num = random.choice(numbers)
combo = str(num)*3
print(combo)