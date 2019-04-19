from common  import is_prime

MAX_NUMBER = 2000000
def get_primes():
    val = 2
    primes = []
    while True:
        if is_prime(val):
            primes.append(val)
        if val >= MAX_NUMBER:
            return primes
        val += 1

print(sum(get_primes()))
