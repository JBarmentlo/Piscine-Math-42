from utils.isbitset import is_bit_set
from utils import single_out

def gray_code(a):
    out = 0
    for i in range(32):
        out = out | (single_out(a, i) ^ (single_out(a, i + 1) >> 1))
    return out