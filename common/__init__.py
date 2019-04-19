import math

def is_prime(number):
  upper_limit = math.ceil(number + 1 / 2)
  for i in range(2, upper_limit):
    if number != i and number % i == 0:
      return False
  return True

def is_palindrome(number):
  arr = str(number)
  mid = int(round(len(arr) / 2))
  for i in range(0, mid):
    if arr[i] != arr[len(arr) - i - 1]:
      return False
  return True

def is_pythogarean_triplet(a, b, c):
  return Math.pow(a, 2) + Math.pow(b, 2) == Math.pow(c, 2)