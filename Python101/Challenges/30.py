print("Challenge 30: WAF program to find the digits which are absent in a given mobile number.")

mobile = input('Please enter a mobile number: ' )
all = '0123456789'
print('missing digits are ', set(all) - set(mobile))