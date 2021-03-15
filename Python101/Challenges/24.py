print("Choose the side you want the calculate!")
print("""            |\\
            | \\
            |  \\
         A  |   \\ C
            |    \\
            |_____\\ 
              B   """)


import math
side = input("The inputs are : A or B or C : ")
side = side.upper()
if side == "A":
    while 1:
        B = input("Please provide the length of value B : ")
        try:
            B = float(B)
            break
        except ValueError:
            print("Enter an integer please!")
    while 1:
        C = input("Please provide the length of value C : ")
        try:
            C = float(C)
            break
        except ValueError:
           print("Enter an integer please!")

    A = math.sqrt(C**2 - B**2)
    print("A is {}".format(A))
elif side == "B":
    while 1:
        A = input("Please provide the length of value A : ")
        try:
            A = float(A)
            break
        except ValueError:
            print("Enter an integer please!")

    while 1:
        C = input("Now enter the length of value C : ")
        try:
            C = float(C)
            break
        except ValueError:
            print("Enter an integer please!")

    B = math.sqrt(C**2 - A**2)
    print("B lengh is {}".format(B))
    
    
elif side=="C":
    while 1:
        B = input("Now enter the length of value B : ")
        try:
            B = float(B)
            break
        except ValueError:
            print("Enter an integer please!")

    while 1:
        A = input("Now enter the length of value A: ")
        try:
            A = float(A)
            break
        except ValueError:
            print("Enter an integer please!")
    C = math.sqrt(A**2 + B**2)
    print("C lengh is {}".format(C))
else:
    print("You have choose a wrong input. Options: A, B or C")
