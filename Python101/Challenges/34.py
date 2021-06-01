print("Challenge 34: WAF to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure.")

num = 583
reversed_num = int(str(num)[::-1])
result = num + reversed_num

while result != int(str(result)[::-1]):
    result = result + int(str(result)[::-1])
    print(result)