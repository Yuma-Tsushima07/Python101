print("Challenge 42: Write a Python program that accepts six numbers as input and sorts them in descending order.")


def main():
    # List of numbers
    listOfNum = [8, 19, 27, 67, 456, 1234, 98]
    print("Initial List", listOfNum,  sep='\n')
    # Create a sorted copy of existing list
    newList = sorted(listOfNum)
     # print the List
    print("New List", newList,  sep='\n')
     # print the List
    print("Existing List", listOfNum,  sep='\n')
    
    # Sort the List in Place
    listOfNum.sort(reverse=True)
    # print the List
    print("List Sorted in Descending Order", listOfNum,  sep='\n')

    if __name__ == "__main__":
        main()