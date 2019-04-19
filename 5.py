

success = False


def is_divisible(val):
  for i in [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]:#range(1,10):
    if val % i != 0:
      return False
  return True

def get_least_common_nominator(nbr):
  while True:
    if is_divisible(nbr):
      return nbr
    nbr = nbr + 20

print(get_least_common_nominator(20))