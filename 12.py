from common import e_sieve, get_nbr_divisors_prime

primes = e_sieve(1000)

nbr_of_divisors = 500
k = 2
even = 2
odd = 2
count = 0
while count < nbr_of_divisors:
    if k % 2 == 0:
        even = get_nbr_divisors_prime(k + 1, primes)
    else:
        odd = get_nbr_divisors_prime((k + 1)/2, primes)
    count = even * odd
    k += 1

print(k*(k-1) / 2)