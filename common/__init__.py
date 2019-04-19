import math

def is_prime(n):
  if n == 2:
    return True
  if n == 3:
    return True
  if n % 2 == 0:
    return False
  if n % 3 == 0:
    return False

  i = 5
  w = 2
  while i * i <= math.ceil(math.sqrt(n)):
    if n % i == 0:
      return False
    i += w
    w = 6 - w
  return True

def is_palindrome(number):
  arr = str(number)
  mid = int(round(len(arr) / 2))
  for i in range(0, mid):
    if arr[i] != arr[len(arr) - i - 1]:
      return False
  return True

def is_pythogarean_triplet(a, b, c):
  return math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)

def parse_string_matrix(matrix):
  ret_val = []
  for row in matrix.split('\n'):
    x = []
    for num in row.split(' '):
      x.append(int(num))
    ret_val.append(x)
  return ret_val
