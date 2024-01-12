from collections import Counter


def ana(a, b):
    return "YES" if sorted(a) == sorted(b) else "NO"


# a = "geeksforgeeks"
# b = "forgeeksgeeks"

a = "geeksforgeeks"
b = "forgeeksgeeks"

res = ana(a, b)
print(res)
