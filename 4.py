from common import is_palindrome

nbr = 999
success = False

def max_palindrome():
  palindromes = []
  for i in range(1, nbr):
    for j in range(1, i + 1):
      left = nbr - i
      right = nbr - j
      if is_palindrome(left * right):
        palindromes.append(left * right)
  return max(palindromes)
print(max_palindrome())