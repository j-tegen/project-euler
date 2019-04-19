from common import is_pythogarean_triplet

first_thousand = range(1, 1000)
sums_to_thousand = []
for a in range(1, 1000):
  for b in range(a, 1000 ):
    for c in range(a + b, 1000):
      if a + b + c == 1000:
        sums_to_thousand.append([a, b, c])

print(sums_to_thousand)