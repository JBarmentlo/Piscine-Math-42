def single_out(a, index):
    '''
        returns a with all bits but the index bit set to 0
    '''
    return (a & (1 << index))