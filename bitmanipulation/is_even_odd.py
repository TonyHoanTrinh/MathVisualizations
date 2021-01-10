def is_even_odd(x: int):
    if x & 1 == 0:
        return "Even"
    else:
        return "Odd"

# Yields Even:
print(is_even_odd(26))

# Yields Odd:
print(is_even_odd(25))
