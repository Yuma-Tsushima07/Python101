print("Challenge 5: WAF that takes a input n and computer n+nn+nnn.")
y = int(input("Input an integer : "))
n1 = int( "%s" % y )
n2 = int( "%s%s" % (y,y) )
n3 = int( "%s%s%s" % (y,y,y) )
print (n1+n2+n3)