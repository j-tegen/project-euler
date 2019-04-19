from common import is_pythogarean_triplet

first_thousand = range(1, 1000)
sums_to_thousand = []
for a in range(1, 1000):
  for b in range(1, 1000 - a ):
    sums_to_thousand.append({ 'a': a, 'b': b, 'c': 1000 - a - b})

for val in sums_to_thousand:
  if is_pythogarean_triplet(val['a'], val['b'], val['c']):
    print(val['a'] * val['b'] * val['c'])
    break