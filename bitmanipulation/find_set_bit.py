"""
Given a number having only one '1' and all other '0's in its binary representation, find position of the only set bit. Assume we begin counting the position from the right and start counting at 0.
"""

import math

def is_power_of_two(n):
    return math.log(n, 2) == math.floor(math.log(n, 2))

def find_set_bit(n):
    if not is_power_of_two(n):
        return -1
    
    pos_count = 0
    while n:
        n >>= 1
        pos_count += 1

    return pos_count

n = 16
print(bin(n)[2:])
print(find_set_bit(n))
