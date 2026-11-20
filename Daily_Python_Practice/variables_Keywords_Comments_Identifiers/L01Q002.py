# Rotate three variables so a, b, c = 1, 2, 3 becomes 2, 3, 1.
a, b, c = 1, 2, 3
a, b, c = b, c, a
print(a, b, c) # 2 3 1