print('Challenge 14: WAF to check if a number is present in a list or not.')

first = input("Please enter the split you'd like to use:")
if "," in first:
  first = first.split(",")
else:
  first = first.split()