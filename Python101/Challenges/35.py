print("Challenge 35: WAF program to check whether three given lengths (integers) of three sides form a right triangle. Print 'Yes' if the given sides form a right triangle otherwise print 'No'.")

sides = input('Enter the 3 sides of triangle separated by spaces: ')
s = [int(i) for i in sides.split(' ')]
x, y, z = s
test = [x**2==y**2+z**2, y**2==x**2+z**2, z**2==x**2+y**2]
if True in test: print('Yes')
else: print('No')