print("Challenge 41: WAPP to compute and print sum of two given integers (more than or equal to zero). If given integers or the sum have more than 80 digits, print 'overflow'.")


print("Input first integer:")
a=int(input())
print("Input second integer:")
b=int(input())
if len(str(a))>80 or len(str(b))>80 or len(str(a+b))>80:
    print("Overflow")
else:
    print("Sum of the two integers:",a+b)