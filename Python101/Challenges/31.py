print("Challenge 31: WAF program to find the type of the progression (arithmetic progression/geometric progression) and the next successive member of a given three successive members of a sequence.")

def ap(l1):
    l = []
    for i, v in enumerate(l1):
        if i != len(l1) - 1:
            l.append(l1[i + 1] - l1[i])
            if len(set(l)) == 1:
                print("It's an AP")


def gp(l2):
    l = []
    for i, v in enumerate(l2):
        if i != len(l2) - 1:
            l.append(l2[i + 1] / l2[i])
            if len(set(l)) == 1:
                print("It's an GP")


l1 = [3, 5, 7, 9, 11, 13]
l2 = [2, 6, 18, 54]

ap(l1)
gp(l2)