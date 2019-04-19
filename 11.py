from data import raw_matrix
from common import parse_string_matrix
from numpy import product

matrix = parse_string_matrix(raw_matrix)

def get_lines(x, y):
    lines = []
    if x < 17:
        lines.append([{'x': val, 'y': y} for val in range(x, x + 4)])
    if y < 17:
        lines.append([{'x': x, 'y': val} for val in range(y, y + 4)])
    if x < 17 and y < 17:
        lines.append([{'x': x + val, 'y': y + val} for val in range(0, 4)])
    if x > 3 and y < 17:
        lines.append([{'x': x - val, 'y': y + val} for val in range(0, 4)])
    if x < 17 and y > 3:
        lines.append([{'x': x + val, 'y': y - val} for val in range(0, 4)])
    return lines

def get_all_lines():
    lines = []
    for x in range(0, 20):
        for y in range(0, 20):
            lines += get_lines(x, y)
    return lines

def get_max_line_sum(lines, matrix):
    max_sum = 0
    for line in lines:
        points = [matrix[point['x']][point['y']] for point in line]
        max_sum = max([max_sum, product(points)])
    return max_sum

lines = get_all_lines()
print(get_max_line_sum(lines, matrix))
