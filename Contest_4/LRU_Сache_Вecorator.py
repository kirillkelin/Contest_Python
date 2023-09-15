import functools


def cache(max_size):
    def decorator(func):
        cache_dict = {}
        cache_list = []

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache_dict:
                cache_list.remove(key)
                cache_list.insert(0, key)
                return cache_dict[key]
            else:
                result = func(*args, **kwargs)
                cache_dict[key] = result
                cache_list.insert(0, key)

                if len(cache_list) > max_size:
                    oldest_key = cache_list.pop()
                    del cache_dict[oldest_key]

            return result

        return wrapper

    return decorator


@cache(3)
def expensive_calculation(x, y):
    result = x + y
    return result


print(expensive_calculation(1, 3))
print(expensive_calculation(2, 4))
print(expensive_calculation(3, 5))
print(expensive_calculation(1, 3))
print(expensive_calculation(2, 2))
