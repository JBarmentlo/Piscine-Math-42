def is_bit_set(a:  int, offset: int):
    '''
        bit indices start a 0 for the rightmost bit
    '''
    return ((a >> offset) & 1) == 1