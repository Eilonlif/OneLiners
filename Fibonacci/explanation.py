from fibonacci import f


def fibonacci(n):
    # Helper function
    def help_fibo(a, b, n):
        if not n:
            return a + b
        return help_fibo(b, a + b, n - 1)

    # Edge case
    if n - 1 > 0:
        return help_fibo(0, 1, n - 2)
    return n


print(fibonacci(5))
print(f(5))
