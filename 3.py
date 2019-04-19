from common import is_prime
import math


def get_divisors(number):
  divisors = []
  upper_limit = math.ceil(number / 2)
  for i in range(2, upper_limit):
    if not is_prime(i):
      continue

    if number % i == 0:
      number = round(number / i)
      upper_limit = math.ceil(number / 2)
      divisors.append(i)
    if number == 1:
      return divisors


number = 600851475143
divs = get_divisors(number)

print(max(divs))
