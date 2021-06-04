print('Challenge 6: WAF to check if number is between 100, 1000 or 10000.')



X = 100
Y = 1000

def checkRange(num):
   # using comaparision operator
   if X <= num <= Y:
       print('The number {} is in range ({}, {})'.format(num, X, Y))
   else:
      print('The number {} is not in range ({}, {})'.format(num, X, Y))

# Test Input List
testInput = [X-1, X, X+1, Y+1, Y, Y-1]

for eachItem in testInput:
   checkRange(eachItem)


Y = 100
Z = 10000

def checkRange(num):
   # using comaparision operator
   if Y <= num <= Z:
       print('The number {} is in range ({}, {})'.format(num, Y, Z))
   else:
      print('The number {} is not in range ({}, {})'.format(num, Y, Z))

# Test Input List
testInput = [Y-1, Y, Y+1, Z+1, Z, Z-1]

for eachItem in testInput:
   checkRange(eachItem)