print("Challenge 33: WAF program to find common divisors between two numbers in a given pair.")

def cd(x,y):
    result = []
    for dx in range(1,x+1):
        for dy in range(1,y+1):
            if x%dx == 0 and y%dy == 0 and dx==dy:
                result.append(dx)
            return result
a = cd(12,24)
print("common divisors: ", a, "\nnumber of common divisors: ", len(a))