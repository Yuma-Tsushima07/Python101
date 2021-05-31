print("Challenges 23: Write a Python program to create all possible permutations from a given collection of distinct numbers.")

X = [1,2,3]
result=[]
for a in X:
    for b in X:
        for c in X:
            if (a+b+c)==sum(X) and a!=b!=c:
                perm=(a,b,c)
                result.append(perm)
                print(result)