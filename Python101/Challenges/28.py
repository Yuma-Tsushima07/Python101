import sys
print("Challenge 28: WAF program to create a sequence where the first four members of the sequence are equal to one, and each successive term of the sequence is equal to the sum of the four previous ones. Find the Nth member of the sequence.")

def sequence(n):
    i = 0
    x = 0
    list = [1, 1, 1, 1]
    while i != n:
        for y in list[int(i):]:
            x += y
            i += 1
        list.append(x)
    return list


def main(n):
    for x in sequence(n):
        print(x)

if __name__ == "__main__":
    try:
        main(int(sys.argv[1]))
    except ValueError:
        print(f"{sys.argv[1]} is not an integer")
        exit()