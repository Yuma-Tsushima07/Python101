print("Challenge 29: WAF program to find the number of divisors of a given integer")

def divisor(n):
    count = 0
    for div in range(1,n+1):
        if n % div == 0:
            count += 1
            return count
n = 20
print ("Total Divisors of %d are: %d" %(n, divisor(n)))