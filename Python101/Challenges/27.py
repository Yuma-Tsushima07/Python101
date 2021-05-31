print("Challenge 27: WAF program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against a given amount.")

def notes(a):
  Q = [500, 200, 100, 50, 20, 10]
  x = 0
  for i in range(6):
    q = Q[i]
    x += int(a / q)
    a = int(a % q)
  if a > 0:
    x = -1
  return x
print(notes(880))
print(notes(1000))