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

def get_divisors(number, known_divisors):
  max_divisor = math.ceil(number/2)
  divisors = []
  for i in range(max_divisor, 2, -1):
    if number % i != 0:
      continue
    if known_divisors.get(i, None):
      divisors += known_divisors[i][0:-1]
      break
    divisors.append(i)
  divisors = [number] + divisors + [1]
  known_divisors = set_known_divisors(divisors, known_divisors)
  return divisors

def set_known_divisors(divisors, known_divisors):
  if len(divisors) == 0:
    return known_divisors
  new_known_divisors = known_divisors

  for k in divisors:
    new_known_divisors.pop(k, None)
  new_known_divisors[divisors[0]] = divisors
  return new_known_divisors

def dict_contains_key(dictionary, key):
  if dictionary.get(key, None):
    return True
  return False


def improved_get_divisors(number, known_divisors = {}):
  max_divisor = math.ceil(number/2)
  divisors = []
  if known_divisors.get(number, None):
    return known_divisors

  for i in range(max_divisor, 1, -1):
    if number % i == 0:
      divisors.append(i)
      divisors += improved_get_divisors(i, known_divisors)
      return divisors
  return divisors + [1]

def get_next_triangle(previous, i):
  return previous + i

def e_sieve(max_number):
  upper_sqrt = int(round(math.sqrt(max_number)))
  prime_map = [True for val in range(0, max_number)]
  for i in range(2, upper_sqrt + 1):
    if prime_map[i]:
      j = i*i
      while j < max_number:
        prime_map[j] = False
        j += i
  return ([index for index, val in enumerate(prime_map) if val])[2:]

def get_prime_divisors(number, prime_list):
  i = 0
  divisors = []
  for i in range(0, len(prime_list)):
    while number % prime_list[i] == 0:
      number = number / prime_list[i]
      divisors.append(prime_list[i])
  return divisors

def get_nbr_divisors_prime(number, prime_list):
  i = 0
  nbr_divisors = 1
  for i in range(0, len(prime_list)):
    exponent = 0
    while number % prime_list[i] == 0:
      number = number / prime_list[i]
      exponent += 1
    nbr_divisors *= (exponent + 1)
  return nbr_divisors

def is_power_of_two(nbr):
  log_nbr = math.log(nbr, 2)
  if math.floor(log_nbr) == math.ceil(log_nbr):
    return True
  return False