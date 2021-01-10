def set_nth_bit(x: int, n: int):
    # If you just want to return the binary represent of the number:
    # return bin(x | 1 << n)[2:]
    return x | 1 << n

print(set_nth_bit(6, 0))
