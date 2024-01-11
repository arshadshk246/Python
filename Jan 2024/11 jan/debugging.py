def reverse(x):
    x = str(x)
    rev = x[::-1]
    x = int(rev)
    return x


res = reverse(123)
print(res)
