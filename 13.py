from data import hundred_50_digits

part_sum = sum([int(val[0:15]) for val in hundred_50_digits.split('\n')])
print(str(part_sum)[0:10])