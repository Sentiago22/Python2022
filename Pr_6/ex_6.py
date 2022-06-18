def make_perf(counter):
    def decorator(func):
        func_name = func.__name__

        def wrapper(*args):
            counter[func_name] = counter.get(func_name, 0) + 1
            res = func(*args)
            return res

        return wrapper

    return decorator


PERF = {}

perf = make_perf(PERF)


@perf
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


@perf
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fact(10))
print(fib(27))
print(PERF)
