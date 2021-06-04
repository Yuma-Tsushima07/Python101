from datetime import date
print("HOTS Challenge 3: WAF to calculate number of days between 2 dates.")


f_date = date(2021, 8, 6)
l_date = date(2021, 8, 12)
delta = l_date - f_date
print(delta.days)