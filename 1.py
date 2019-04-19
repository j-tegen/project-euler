max_number = 10000
divisors = [3, 5]

min_divisor = min(divisors)
sum = 0

def check_divisable(number, divisors):
  return len([div for div in divisors if number % div == 0]) > 0

for i in range(min_divisor, max_number):
  if check_divisable(i, divisors):
    sum += i


print(sum)