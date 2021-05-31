import re

print('Challenge 13: WAF to remove all the vowles from a string.')


vowels = 'aeiouAEIOU'

given_str = input("Enter a string : ")
translate = str.maketrans(dict.fromkeys(vowels))

final_str = given_str.translate(translate)

print(final_str)