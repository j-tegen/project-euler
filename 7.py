from common import is_prime


def get_nth_prime(n):
  NBR_PRIMES = 0
  i = 2
  while True:
    if is_prime(i):
      NBR_PRIMES += 1
    if NBR_PRIMES == n:
      return i
    i += 1

print(get_nth_prime(10001))