import math
print("Challenge 37: WAF to compute the amount of the debt in n months. The borrowing amount is $100,000 and the loan adds 5% interest of the debt and rounds it to the nearest 1,000 above month by month.")


x=100000
for i in range(7):
    x=math.trunc(x*.05+x)
if x%1000==0:
    x=x
else:
    x=(1000-(x%1000))+x
print(x)