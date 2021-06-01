def adder(a, b):
    '''
        xor the bits that add to 1, ret the bits that add to two (retenue)
    '''
    xor = a ^ b
    ret = a & b
    ret = ret << 1
    while (ret & xor != 0):
        tmp = ret ^ xor
        ret = (ret & xor) << 1
        xor = tmp
    return xor | ret


def add(*ints):
    if len(ints) == 0:
        raise ValueError
    out = 0
    for i in range(len(ints)):
        out = adder(out, ints[i])
    return (out)



