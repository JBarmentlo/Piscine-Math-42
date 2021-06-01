from X00_adder import add
from utils import is_bit_set

def multiply(a, b):
    out = 0
    for i in range(32):
        if (is_bit_set(b, i)):
            out = add(out, a << i)
    return out


