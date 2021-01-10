def unset_rightmost_set_bit(x: int):
    return x & (x - 1)

# Unset rightmost bit of binary representation of 7:
y = unset_rightmost_set_bit(7)
print(y)
