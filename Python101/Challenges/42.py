print("Challenge 42: Write a Python program that accepts six numbers as input and sorts them in descending order.")

print("Input six integers:")

nums = list(map(int, input().split()))
nums.sort()
nums.reverse()

print("After sorting the said integers:")
print(*nums)