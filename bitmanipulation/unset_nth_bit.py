def unset_nth_bit(x: int, n: int):
    # If you just the binary representation of the number:
    # return bin(x & ~(1 << n))[2:]
    return x & ~(1 << n)

# Unset 1st bit of in binary representation of 6:
print(unset_nth_bit(6, 1))

# Unset 2nd bit of in binary representation of 6:
print(unset_nth_bit(6, 2))

