import math
from common import is_power_of_two


def get_seq_len(nbr, seqs):
    seq_len = 0
    while nbr != 1:
        if is_power_of_two(nbr):
            seq_len += math.log(nbr, 2) + 1
            return seq_len
        if seqs.get(nbr, None):
            return seqs_lens
        if nbr % 2 == 0:
            nbr = nbr / 2
        else:
            nbr = nbr * 3 + 1
        seq_len += 1
    return seq_len

MAX_NBR = 1000000
max_seq_len = 0
max_seq_nbr = 1
seqs_lens = {}


for i in range(1, MAX_NBR):
    seq_len = get_seq_len(i, seqs_lens)
    if seq_len > max_seq_len:
        seqs_lens[i] = seq_len
        max_seq_len = seq_len
        max_seq_nbr = i

print(max_seq_len)
print(max_seq_nbr)