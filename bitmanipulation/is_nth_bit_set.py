def is_nth_bit_set(x: int, n: int):
    if x & (1 << n):
        return True
    return False

# Is 2nd bit set for binary representation of 6: (True)
print(is_nth_bit_set(6, 2))

# Is 0th bit set for binary representation of 6: (False)
print(is_nth_bit_set(6, 0))

