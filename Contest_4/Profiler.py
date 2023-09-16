import time
import functools


def profiler(func):
    profiler.calls = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        behind_calls = profiler.calls
        profiler.calls += 1

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        wrapper.last_time_taken = end_time - start_time
        wrapper.calls = profiler.calls - behind_calls

        return result

    return wrapper


@profiler
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


result2 = ackermann(3, 4)
print(result2)
print(ackermann.calls)
result1 = ackermann(1, 2)
print(result1)
print(ackermann.calls)
result3 = ackermann(3, 4)
print(result3)
print(ackermann.calls)
print(ackermann.last_time_taken)
