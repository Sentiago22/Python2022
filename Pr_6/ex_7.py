def make_perf(counter):
    def decorator(func):
        func_name = func.__name__

        def wrapper(*args):
            counter[func_name] = counter.get(func_name, 0) + 1
            res = func(*args)
            return res

        return wrapper

    return decorator


def memo(func):
    global
    dp = {}

    def wrapper(*args):
        val = args[0]
        if not dp.get(val):
            dp[val] = func(val)
        return dp.get(val)
    return wrapper


PERF = {}

perf = make_perf(PERF)


@memo
@perf
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


@memo
@perf
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fact(10))
print(fib(5))
print(PERF)
print(dp)