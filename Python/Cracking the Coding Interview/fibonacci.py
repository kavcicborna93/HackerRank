def fibonacci(n,memo={}):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    try:
        return memo[n]
    except:
        result = fibonacci(n-1,memo) + fibonacci(n-2,memo)
        memo[n] = result
        return result

n = int(input())
print(fibonacci(n))
