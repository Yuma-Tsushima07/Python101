print("HOTS Challenge 1: Write a Python program to count the number of carry operations for each of a set of addition problems.")

num = 10
num2 = 10

if len(str(num)) != len(str(num2)):
      len_difference = abs(len(str(num)) - len(str(num2)))
      smaller_value = min(num, num2)
      smaller_value = (str(0) * len_difference) + str(smaller_value)
      bigger_value = max(num, num2)

else:
      smaller_value = min(num, num2)
      bigger_value = max(num, num2)
      
count = 0
carry = 0
for x,y in zip(reversed(str(smaller_value)), reversed(str(bigger_value))):
      if (int(x) + int(y) + carry) >= 10:
            count += 1
            carry = 1
      
      else:
            carry = 0

print(count)