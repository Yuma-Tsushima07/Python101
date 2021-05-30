print("WAF to input a list and WAF to print first and last element of the list.")
list = [1,2,3,4,5,6,7,8,9,10]
ans = list[::len(list)-1]
print ("The first and last elements of the list are : " + str(ans))
