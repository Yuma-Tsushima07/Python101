print("Challenge 20: WAP program to find unique triplets whose three elements gives the sum of zero from an array of n integers.")

def unique_tripplets(number_list):
    for i in range(len(number_list) - 2):
        if len(number_list[i:i + 3]) == len(set(number_list[i:i + 3])) and sum(number_list[i:i + 3]) == 0:
            print(number_list[i:i + 3])

unique_tripplets([1, -6, 4, 2, -1, 2, 0, -2, 0])