import math

print('Challenge 16: WAF to calculate area or triangle')

def AreaOfTriangle(a, b, c):
    s = (a + b + c) / 2
    Area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    print(" The Area of a Triangle is %0.2f" %Area)
     
 
a = float(input('Please Enter the First side of a Triangle: '))
b = float(input('Please Enter the Second side of b Triangle: '))
c = float(input('Please Enter the Third side of c Triangle: '))
 
AreaOfTriangle(a, b, c)