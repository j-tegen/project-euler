from common import is_prime, e_sieve
import time
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

start = time. time()
print(sum(get_primes()))
end = time. time()
print(end - start)

start = time. time()
print(sum(e_sieve(MAX_NUMBER)))
end = time. time()
print(end - start)