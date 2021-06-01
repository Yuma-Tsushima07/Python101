print("Challenge 32: WAF program to print the length of the series and the series from the given 3rd term, 3rd last term and the sum of a series.")

def ex28(): 
    tn = int(input("Input third term of the series:"))
    tltn = int(input("Input 3rd last term:"))
    s_sum = int(input("Sum of the series:"))
    n=int(s_sum*2/(tn+tltn))
    print('length of the series is',n)
    if n-5==0:
        step = (s_sum-3*tn)//6

    else:
        step = (tltn-tn)/(n-5) 
        a = tn-2*step 
        S =[]
        for i in range(n):
            S.append(int(a))
            a+=step
            print('series:',S)

ex28()