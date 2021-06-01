print("Challenges 38: WAF program to print the number of prime numbers which are less than or equal to a given integer.")

n = 7
nums = range(2, n+1)
num_of_divisors = 0
counter = 0

for x in nums:
    for i in range(1, x+1):
        if x % i == 0:
            num_of_divisors += 1

if num_of_divisors == 2:
    counter += 1

num_of_divisors = 0
print(counter)