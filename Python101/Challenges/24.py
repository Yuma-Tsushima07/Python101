print("choose which side you want to calculate")
print("      /|")
print("     / |")
print("    /  |")
print(" C /   |  A")
print("  /    |")
print(" /     |")
print("/______|")
print("    B")
import math
side = input("input be like : A or B or C : ")
side = side.upper()
if side == "A":
    while 1:
        B = input("enter B lengh : ")
        try:
            B = float(B)
            break
        except:
            print("please enter an integer ....")
    while 1:
        C = input("now enter C lengh : ")
        try:
            C = float(C)
            break
        except:
            print("please enter an integer ....")

    A = math.sqrt(C**2 - B**2)
    print("A is {}".format(A))
elif side == "B":
    while 1:
        A = input("enter A lengh : ")
        try:
            A = float(A)
            break
        except:
            print("please enter an integer ....")

    while 1:
        C = input("now enter C lengh : ")
        try:
            C = float(C)
            break
        except:
            print("please enter an integer ....")

    B = math.sqrt(C**2 - A**2)
    print("B lengh is {}".format(B))
    
    
elif side=="C":
    while 1:
        B = input("enter B lengh : ")
        try:
            B = float(B)
            break
        except:
            print("please enter an integer ....")

    while 1:
        A = input("now enter A lengh : ")
        try:
            A = float(A)
            break
        except:
            print("please enter an integer ....")
    C = math.sqrt(A**2 + B**2)
    print("C lengh is {}".format(C))
else:
    print("wrong input buddy , i said : A , B or C ! :(")
