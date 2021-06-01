print("Challenge 36: WAF which solve the equation: Go to the editor ax+by=c dx+ey=f Print the values of x, y where a, b, c, d, e and f are given.")

values = '8 9 7 6 6 5'

values = list(map(float, values.split()))
a,b,c,d,e,f = values

y = ((c*d) - (f*a)) / ((b*d) - (e*a))
x = ((f*a) - (c*d)) / ((b*d) - (e*a))

print(f'x: {x:.3f}', f'y: {y:.3f}', sep='\n')