def toggle_nth_bit(x: int, n: int):
    return x & (1 << n)

# Toggle the 0th bit of the binary representation of 6:
y = toggle_nth_bit(6, 0)
print(y)

# Toggle the 0th bit of the binary representation of 7:
z = toggle_nth_bit(y, 0)
print(z)
