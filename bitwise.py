# Program to demonstrate left shift and right shift operators

number = 8   # binary: 1000

# Left shift (<<) : shifts bits to the left, adds zeros on the right
left_shift = number << 2   # equivalent to number * 2^2

# Right shift (>>) : shifts bits to the right, discards bits on the right
right_shift = number >> 2  # equivalent to number // 2^2

print("Original number:", number)
print("Left shift by 2:", left_shift)
print("Right shift by 2:", right_shift)
