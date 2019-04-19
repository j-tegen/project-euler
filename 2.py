MAX_NUMBER = 4000000


sum = 0
first = 1
second = 1
while first < MAX_NUMBER:
  if first % 2 == 0:
    sum += first

  tmp = first + second
  second = first
  first = tmp

print(sum)