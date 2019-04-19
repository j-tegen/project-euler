import math
max_nbr = 101
arr = range(1, max_nbr)
sum_square = math.pow(sum(arr),2)
part_square = sum([math.pow(val, 2) for val in arr])
print(sum_square - part_square)
