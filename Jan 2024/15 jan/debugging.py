def fib(num, memo={}):
    if num in memo:
        return memo[num]
    if num == 0:
        return 0
    if num == 1:
        return 1
    result = fib(num - 1, memo) + fib(num - 2, memo)
    memo[num] = result
    return result


res = fib(50)
print(res)
